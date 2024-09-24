# Localization-with-LoRa-internship24
This repository has the coding files related to my tasks during my internship at the GUC IET department as a Research Assistant intern. It is also a documentation for whoever will complete working on the research project.

## Research project
- A Localization device using LoRa technology under the supervision of Prof.Tallal Elshabrawy.

## Summary of my tasks
- Migration of signal analysis and real-time plotting to ThingsBoard platform, as I proposed solutions using the platform and created the needed customized Dashboards
- Testing of LoRa and LoRa-GPS modules using Arduino and python scripts.
- Implemented a prototype of the device in research, using Laptop temperature readings as data that are sent to the Thingsboard platform to plot data in real-time , setting a warning threshold of temp>value using thingsboard customized rule-chain that I did implement, once the threshold is reached; ThingsBoard publishes (broadcasts) an encoded message on a certain frequency through LoRa module, the message can be received by any edge within the transmitting region , once the message is received, it is decoded by a python script to be a warning that the temperature reached the threshold.
