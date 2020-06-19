# if running on a notebook you may need to install a few things: 
# !pip3 install gitpython kfp

import datetime
import kfp as kfp

import kfp.components as comp
import git
repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha

# Modeled after https://github.com/kubeflow/pipelines/blob/master/samples/core/lightweight_component/lightweight_component.ipynb
# General note debugging a pipeline is a pain because man fields don't
# exist until run-time

import comp_1 as comp_1
import comp_2 as comp_2

#might as well keep components a common variable in case you want to write multiple pipelines
comp_1_op=comp.func_to_container_op(comp_1.run,base_image=f"docker.io/mohsseha/comp_1:{sha}")
comp_2_op=comp.func_to_container_op(comp_2.run,base_image=f"docker.io/mohsseha/comp_2:{sha}")    


import kfp.dsl as dsl
@dsl.pipeline(
   name='Simple Calculation pipeline',
   description='simple example that composes a couple of ops with different source packages'
)
def experiment_pipeline(
   in_1=3.1,
   in_2=323.1,
   username='random_username',
):
    #Passing pipeline parameters to operation: 
    comp_1_task=comp_1_op(in_1,in_2)
    
    #Passing a task output reference as operation arguments
    #For an operation with a single return value, the output reference can be accessed using `task.output` or `task.outputs['output_name']` syntax
    comp_2_task = comp_2_op(comp_1_task.outputs['result'], username)
    print(f"this is run @ compile time not runtime  {comp_2_task.output}")





#Specify pipeline argument values
args = {
   "in_1":3.1,
   "in_2":323.1,
   "username": 'random_username'
}
now=datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")

# compiling is optional; you really should not be doing it regularly 
kfp.compiler.Compiler().compile(experiment_pipeline,"experiment_pipeline.yaml")

#Submit a pipeline run 
#kfp.Client().create_run_from_pipeline_func(experiment_pipeline, arguments=args,run_name=now,experiment_name="simple_Poc")

