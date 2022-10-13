1. You'll need to make an account on Hugging Face, and navigate to [this page](https://huggingface.co/CompVis/stable-diffusion-v1-4) and accept the license before continuing!

2. You'll need to ensure you have `git-lfs`: 

<details><summary>Install on Linux</summary>
```sudo apt install git-lfs```
</details>

<details><summary>Install on Mac</summary>
https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage
</details>

<details><summary>Install on WSL2</summary>
```sudo apt-get install git-lfs```
</details>

3. After you have `git-lfs`, you can install it with:

```git lfs install```

4. Now you can create a new directory in your repository called: `models` with a command like:

```mkdir models```

5. You'll want to `cd models`

6. The next step will prompt your to log-into your Hugging Face account, and will take quite some time! (You need to download the 4GB of model checkpoint!)

```git clone https://huggingface.co/CompVis/stable-diffusion-v1-4```

7. You should be good, from this point, to build, and run the Dockerfile using the commands:

```docker build -t stable_diff_cpu .```

and 

```docker run --rm -p 5000:5000 stable_diff_cpu```

Inference will take some time, since it's using CPU - but you'll be good to go after these steps!


