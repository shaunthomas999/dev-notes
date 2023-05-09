# Kafka

## Kafka Tools
 
### Kafdrop

#### Installation

* Download jar from `https://github.com/obsidiandynamics/kafdrop/releases`
  * E.g. https://github.com/obsidiandynamics/kafdrop/releases/download/3.30.0/kafdrop-3.30.0.jar
* Copy the jar to a suitable folder (for me $HOME/Developer/tools/kafdrop)
* Run Kafdrop using the command - `java --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -jar kafdrop-3.30.0.jar`
  * Note the version in the jar file. Use suitable version.
  * Uses default kafka broker url - `localhost:9092`
  * Additional config options are described in `https://github.com/obsidiandynamics/kafdrop#getting-started`
* Open a browser and access Kafdrop UI using URL `localhost:9000`

### Offset Explorer 2

### Kafka Manager

### Intellij IDEA Ultimate - BigData Tools

## Kafka CLI

### Topics
* See details of a topic - `kafka-topics --bootstrap-server localhost:9092 --describe --topic <topic_name>`

### Offsets

See latest offset - `kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic <topic_name>  --time -1`
See earliest offset - `kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic <topic_name>  --time -2`

Reset offset to earliest dry run - `kafka-consumer-groups --bootstrap-server localhost:9092 --group <group_name> --topic <topic_name> --reset-offsets --to-earliest --dry-run`
Reset offset to earliest execute - `kafka-consumer-groups --bootstrap-server localhost:9092 --group <group_name> --topic <topic_name> --reset-offsets --to-earliest --execute`

`--to-latest`
`--to-current`
`--shift-by 1`
`--all-topics`

`kafka-consumer-groups --bootstrap-server localhost:9092 --all-groups --all-topics --reset-offsets --to-earliest --dry-run`
`kafka-consumer-groups --bootstrap-server localhost:9092 --all-groups --all-topics --reset-offsets --to-earliest --execute`



