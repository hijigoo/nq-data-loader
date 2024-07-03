# 명령어

## Cloud9 볼륨 조절
```
cd ~/environment/nq-data-loader
bash resize.sh 50
```

## 프로젝트 다운로드
```
https://github.com/hijigoo/nq-data-loader.git
```

## 파일 다운로드
```
cd ~/environment/nq-data-loader
aws s3 cp <S3 URI> ./data
```

ex)
```
cd ~/environment/nq-data-loader
aws s3 cp s3://coding-school-2024/data/v1.0-simplified-nq-train.jsonl.gz ./data/v1.0-simplified-nq-train.jsonl.gz
```

## 파일 압축 해제
```
cd ~/environment/nq-data-loader/data
gzip -d v1.0-simplified-nq-train.jsonl.gz 
```

## 파일 용량 확인
```
ls -alh
```

## 코드 실행
```
cd ~/environment/nq-data-loader
python nq_loader.py
```

## 코드 실행(with option)
- filepath: v1.0-simplified-nq-train.jsonl 파일 경로입니다
- output_dir: 결과물이 저장될 디렉토리 입니다.
- start: 시작 라인입니다
- end: 멈출 라인입니다. (전체 라인수를 넘어서면, 최대 라인까지만 정제합니다.)
- is_print: 출력내용물이 보일지 여부입니다. (True 로 하는 경우 많은 라인을 정제할 때 속도가 느려집니다)
- is_skip_no_answer: long answer 이 비어있는 파일은 제외할지 여부입니다.
```
cd ~/environment/nq-data-loader
python nq_loader.py --filepath ./data/v1.0-simplified-nq-train.jsonl --output_dir ./data/ --start 0 --end 10 --is_print True --is_skip_no_answer False
```
