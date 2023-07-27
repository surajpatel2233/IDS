# IDS_DDOS 2020-2021

   This workgroup is a project created by 4 students of the University of Visvesvaraya Technological University for the fourth year. 

## Abstract 

The purpose of this project is to develop an artificial intelligence to classify possible DDoS attacks in an SDN network. This will be done by using data collectors such as Telegraf, Mininet to emulate the SDN network, and InfluxDB as a means to store data.

**Keywords**: [`DDoS attacks`](https://www.digitalattackmap.com/); [`SDN network`](https://www.opennetworking.org/sdn-definition/); [`Artificial Intelligence classification`](https://www.sciencedirect.com/science/article/abs/pii/016974399500050X); [`Mininet`](http://mininet.org/)

## Index

- [Installation methods](#installation-methods-wrench)
  * Vagrant
  * Native
- [Our scenario]
  * Running the scenario
  * Is working properly?
    
- [Attack time!]
    + Time to limit the links
    + Getting used to hping3
    + Installing things.
    + Usage
    + Demo time!
    + Wanted a video?
   
- [Traffic classification with a SVM (**S**upport **V**ector **M**achine)]
  * First step: Getting the data collection to work
  * Second step: Generating the training datasets
  * Third step: Putting it all together: `src/traffic_classifier.py`
- [Mininet CLI (**C**ommand **L**ine **I**nterface)]
- [Mininet Internals]
  * Network Namespaces
- [Mininet Internals (II)
  * Is Mininet using Network Namespaces?
  * The Big Picture
      - How would our Kernel-level scenario look then?
- [Troubleshooting]
- [Appendix]
  * The Vagrantfile
  * File descriptors: `stdout` and friends


