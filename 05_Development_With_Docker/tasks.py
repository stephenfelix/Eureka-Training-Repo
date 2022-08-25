from invoke import task

@task
def build(c):
    c.run("docker build -t super-ros-node .")

