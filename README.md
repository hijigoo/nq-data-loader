# 명령어

## Cloud9 볼륨 조절
```
bash resize.sh 50
```

## 파일 다운로드
```
mkdir data
cd ~/environment/data
aws s3 cp <S3 URI> ./
```

```
ex) aws s3 cp s3://coding-school-2024/data/v1.0-simplified-nq-train.jsonl.gz ./
```


## 파일 압축 해제
```
cd ~/environment/data
gzip -d v1.0-simplified-nq-train.jsonl.gz 
```

## 코드 실행
```
cd ~/environment
python nq_loader.py
```
