# simple-kfp

A simple example on how to build a _light weight_  [KFP](https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/) pipeline. 

This config is maximizing: 
- **simplicity**: Each component should be as close as possible to a python module. ML Engineers don't have time to think of injection etc. 
- **flexibility**: If you need a complex component setup have at it. Just put it in it's own place and modify the pipeline accordingly 
- **less error prone**: components are tagged with the repo's current SHA which should reduce the chances of accidentally calling stale code. 


Should be freindly to inheritence from non-python3 based dockers but you will always need to install python3 in the component container. 

## How to use? 

- Copy `comp_?` to `comp_your_new_component_name` 
- modify the `__init__.py` to have a `run` function 
- add to your graph in the main `pipeline.py` file 
- run as appropriate to generate the YAML or submit to cluster directly. 
