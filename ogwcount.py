# WORD COUNT MAPREDUCE ORIGINAL

bash
start-all.sh
jps

nano input.txt

nano wcmap.py
#!/usr/bin/env python3
import sys
import re
for line in sys.stdin:
    words = re.findall(r'\b\w+\b', line.lower())
    for word in words:
        print(f"{word}\t1")

nano wcred.py
#!/usr/bin/env python3
import sys
current_word = None
current_count = 0
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count
if current_word == word:
    print(f"{current_word}\t{current_count}")

chmod +x wcmap.py wcred.py

cat input.txt | ./wcmap.py | sort | ./wcred.py

hdfs dfs -mkdir /wcount

hdfs dfs -put input.txt /wcount

find / -name "hadoop-streaming*.jar" 2>/dev/null

hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-file wcmap.py -mapper wcmap.py \
-file wcred.py -reducer wcred.py \
-input /wcount/input.txt \
-output /wcount/output

hdfs dfs -cat /wcount/output/part-00000
