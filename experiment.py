import re
import os
import openai
from time import time, sleep
import textwrap


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

# change path to where you store your credentials
openai.api_key = open_file('../creds/creds.txt')
agent = 'me'
workingdir = 'convo_return/'
sumdir = 'summaries/'
agent_model = 'agent.txt'
logdir = 'logs/'


def gpt3_completion(prompt, type, label='gpt3', engine='text-davinci-002', temp=0.99, top_p=1.0, tokens=3000, freq_pen=2.0, pres_pen=2.0, stop=['asdfasdf', 'asdasdf']):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()  # force it to fix any unicode errors
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            text = re.sub('\s+', ' ', text)
            filename = '%s_%s.txt' % (time(), label)
            if type == 'convo':
                dir_c = workingdir
            else:
                dir_c = sumdir
            save_file('%s%s' % (dir_c, filename), text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print('Error communicating with OpenAI:', oops)
            sleep(1)

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def load_convo():
    files = os.listdir(workingdir)
    if files == []:
        return ''
    newest_convo = newest(workingdir)
    result = open_file('%s' % newest_convo).strip()
    return result


def summarize_block(text_block, summary_so_far):
    chunks = textwrap.wrap(text_block, 3000)
    result = list()
    for chunk in chunks:
        prompt = open_file('prompt_summary.txt').replace('<<CONVO>>', chunk).replace('<<SUMMARY>>', summary_so_far)
        summary = gpt3_completion(prompt, type='summary', label='summary', engine='text-davinci-002', temp=0.5)
        result.append(summary)
    summary = '. '.join(result).replace('..', '.')
    return summary



def summarize_convo(convo, i):
    if i == 1:
        summary_so_far = open_file("first_synopsis.txt")
    else:
        newest_summary = newest(sumdir)
        summary_so_far = open_file('%s' % newest_summary).strip()
    summary = summarize_block(convo, summary_so_far)
    return summary


if __name__ == '__main__':
    for i in range(0, 10):
        convo = load_convo()
        print('\n\nSummarizing...')
        if i == 0:
            summary = open_file("first_synopsis.txt")
        else:
            summary = summarize_convo(convo, i)
        print('\n\nSummary:', summary)
        agent = open_file(agent_model)
        prompt = open_file('prompt.txt').replace('<<SUMMARY>>', summary).replace('<<AGENT>>', agent)
        print('\n\nPrompt:', prompt)
        completion = gpt3_completion(prompt, type='convo', label='thought', tokens=2202)
        print('\n\nCompletion:', completion)
        filename = 'log_%s.txt' % time()
        save_file(logdir + filename, prompt + completion)