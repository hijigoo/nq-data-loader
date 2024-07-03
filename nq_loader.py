import sys
import json
import pprint


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


def make_long_answer_text(filepath, output_dir, start, end, is_print, is_skip_no_answer):
    # JSON 파일을 한 번에 모두 읽지 않고 청크(chunk) 단위로 읽기
    line_count = 0
    question_texts = []
    long_answer_texts = []
    with open(filepath, 'r', encoding='utf-8') as f:
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

            if is_skip_no_answer and len(long_answer_text.strip()) == 0:
                continue

            if is_print:
                print_result(question_text=question_text, long_answer_text=long_answer_text)
            question_texts.append(question_text)
            long_answer_texts.append(long_answer_text)

        # Save answers
        save_list_to_txt(f'{output_dir}question_{start}_{line_count - 1}.txt', question_texts)
        save_list_to_txt(f'{output_dir}long_answer_{start}_{line_count - 1}.txt', long_answer_texts)


def main():
    
    # 파라미터 세팅
    filepath = 'data/v1.0-simplified-nq-train.jsonl'
    output_dir = 'data/'
    start = 0
    end = 10
    is_print = False
    is_skip_no_answer = False

    # 명령줄 인수 파싱
    for i, arg in enumerate(sys.argv):
        if arg == "--filepath":
            filepath = sys.argv[i + 1]
        elif arg == "--output_dir":
            output_dir = sys.argv[i + 1]
        elif arg == "--start":
            start = int(sys.argv[i + 1])
        elif arg == "--end":
            end = int(sys.argv[i + 1])
        elif arg == "--is_print":
            is_print = sys.argv[i + 1].lower() == "true"
        elif arg == "--is_skip_no_answer":
            is_skip_no_answer = sys.argv[i + 1].lower() != "false"

    print(f"filepath: {filepath}, output_dir: {output_dir}")
    print(f"start: {start}, end: {end}, is_print: {is_print}, is_skip_no_answer: {is_skip_no_answer}")
    make_long_answer_text(filepath=filepath, output_dir=output_dir, start=start, end=end, is_print=is_print,
                          is_skip_no_answer=is_skip_no_answer)


if __name__ == "__main__":
    main()
