# 명령어
## 프로젝트 다운 로드
```
https://github.com/hijigoo/nq-data-loader.git
```

## Cloud9 볼륨 조절
```
cd ~/environment/nq-data-loader
bash resize.sh 50
```

## 파일 다운로드
```
mkdir data
cd ~/environment/nq-data-loader/data
aws s3 cp <S3 URI> ./
```

```
ex) aws s3 cp s3://coding-school-2024/data/v1.0-simplified-nq-train.jsonl.gz ./
```


## 파일 압축 해제
```
cd ~/environment/nq-data-loader/data
gzip -d v1.0-simplified-nq-train.jsonl.gz 
```

## 코드 실행
```
cd ~/environment/nq-data-loader
python nq_loader.py
```
