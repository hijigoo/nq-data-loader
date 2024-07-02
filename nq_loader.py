import json
import pprint

# JSON 파일 경로
json_file = 'data/v1.0-simplified-nq-train.jsonl'


def print_keys(json_data):
    for key in json_data.keys():
        if key == 'document_text':
            continue
        pprint.pprint(key)
        pprint.pprint(json_data[key])


def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        count = sum(1 for line in file)
    return count


def print_result(question_text, long_answer_text):
    pprint.pprint("================================================")
    print()
    pprint.pprint("QUESTION: ")
    pprint.pprint(question_text)
    print()

    pprint.pprint("LONG ANSWER: ")
    pprint.pprint(long_answer_text)
    print()
    pprint.pprint("================================================")


def save_list_to_txt(filename, text_list):
    with open(filename, 'w+') as file:
        for t in text_list:
            file.write(t + "\n")


def make_long_answer_text(file_path, start, end):
    # JSON 파일을 한 번에 모두 읽지 않고 청크(chunk) 단위로 읽기
    line_count = 0
    question_texts = []
    long_answer_texts = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            if line_count < start:
                continue
            if line_count > end:
                break

            json_data = json.loads(line)

            question_text = json_data['question_text']
            document_text = json_data['document_text']

            annotations = json_data['annotations']
            long_answer_start_token = annotations[0]['long_answer']['start_token']
            long_answer_end_token = annotations[0]['long_answer']['end_token']

            long_answer_text = " ".join(document_text.split(" ")[long_answer_start_token:long_answer_end_token])

            question_texts.append(question_text)
            long_answer_texts.append(long_answer_text)

            # Print Result
            # print_result(question_text=question_text, long_answer_text=long_answer_text)

        # Save answers
        save_list_to_txt(f'data/question_{start}_{line_count-1}.txt', question_texts)
        save_list_to_txt(f'data/long_answer_{start}_{line_count-1}.txt', long_answer_texts)


# Load answers
make_long_answer_text(json_file, start=0, end=10)

