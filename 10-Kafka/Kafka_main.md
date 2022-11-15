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
