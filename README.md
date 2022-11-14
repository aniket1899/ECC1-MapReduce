# ECC1-MapReduce
Query IPs using MapReduce - Fair and Capacity Schedulers, secondary sorting, partitioning


### Setup:
1. Create Jestsream 2 instance (medium). SSH connection to Jetstream 2.
2. Make user "hadoopuser".
3. Give sudo access to "hadoop user".
4. SSH to local-host.
5. Download Hadoop latest version and configure using [this](https://phoenixnap.com/kb/install-hadoop-ubuntu) tutorial.
6. Start using command "start-dfs.sh" and "start-yarn.sh"
7. Run command "jps"

---

### Test wordcount program:


### Part 1:
> Get top 3 IPs for every hour from the log files.

#### Run map-reduce for top 3 on "sample.log":
1. Copy "sample.log", "mapper-ip.py", "reducer-main.py"
2. Run the following command:
   > hadoop jar /home/hadoopuser/hadoop-3.3.4/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar -input /smallLog/sample.log -output /smallLog/output -mapper "python3 /home/hadoopuser/part1/mapper-ip.py" -reducer "python3 /home/hadoopuser/part1/reducer-main.py"

---

### Part 2:
> MapReduce like a query> Query the MapReduce run using command line arguments. User input ‘x-y’ will output top 3 IPsbetween x and y hours (24 hr format).The only change from Part1 is the mapper which accepts command line inputs.


#### Run map-reduce for top 3 on "sample.log":
1. Copy "sample.log", "mapper-ip.py", "reducer-main.py"
2. Run the following command:
   > hadoop jar /home/hadoopuser/hadoop-3.3.4/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar -input /smallLog/sample.log -output /smallLog/output -mapper "python3 /home/hadoopuser/part1/mapper-query.py 3-4" -reducer "python3 /home/hadoopuser/part1/reducer-main.py"
   
 ---
 
### Partitioning:
> Use the following command to *partition* on key 1 i.e., the hour to run the part 1 and part 2 codes efficiently on a multi-cluster Hadoop setup.

Exmaple:
hadoop jar /home/hadoopuser/hadoop-3.3.4/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar  -D stream.num.map.output.key.fields=4 -D mapreduce.partition.keypartitioner.options=-k1,1  -input /accessLog/access.log -output /accessLog/output  -mapper "python3 /home/hadoopuser/part1/mapper-ip.py"  -reducer "python3  /home/hadoopuser/part1/reducer-main.py"  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


### Secondary sort:
> Alternatively use secondary sort on key1:hour ASC and key2:count DESC | NUM

Example:
hadoop jar /home/hadoopuser/hadoop-3.3.4/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar 
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator 
-D stream.num.map.output.key.fields=4  
-D mapred.text.key.partitioner.options=-k1,2 
-D mapred.text.key.comparator.options=-"-k1,1 -k2,2nr" 
-input /accessLog/access.log -output /accessLog/output  -mapper "python3 /home/hadoopuser/bonus/mapper-1.py"  -reducer "python3  /home/hadoopuser/bonus/reducer-2.py"  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

