# pandas_test

## Conda environment

The following command will create an isolated Conda environment for the repository. All packages will be installed into a subdirectory called `./env`. Once you have created the environment you will need to activate it.

```bash
$ conda env create --prefix ./env --file environment.yml
$ source activate ./env
```

On Windows the activate command is slightly different.

```
$ activate ./env
```

## Launching JupyterLab

After activating the environment you can launch the JupyterLab server with the following command.

```bash
$ jupyter lab
```

## Conda deactivate

When you are done, you can deactivate the environment with the following command. This command is the same on Mac OS, Linux, and Windows.

```bash
$ conda deactivate
```
