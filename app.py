{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f62279bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting gradio\n",
      "  Downloading gradio-4.13.0-py3-none-any.whl (16.6 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m16.6/16.6 MB\u001b[0m \u001b[31m10.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hCollecting uvicorn>=0.14.0\n",
      "  Downloading uvicorn-0.25.0-py3-none-any.whl (60 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m60.3/60.3 kB\u001b[0m \u001b[31m2.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: importlib-resources<7.0,>=1.3 in /Users/mariaashby/.local/lib/python3.9/site-packages (from gradio) (5.12.0)\n",
      "Collecting altair<6.0,>=4.2.0\n",
      "  Downloading altair-5.2.0-py3-none-any.whl (996 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m996.9/996.9 kB\u001b[0m \u001b[31m8.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: packaging in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (21.3)\n",
      "Requirement already satisfied: pandas<3.0,>=1.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (1.4.4)\n",
      "Collecting python-multipart\n",
      "  Downloading python_multipart-0.0.6-py3-none-any.whl (45 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m45.7/45.7 kB\u001b[0m \u001b[31m1.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: markupsafe~=2.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (2.0.1)\n",
      "Collecting tomlkit==0.12.0\n",
      "  Downloading tomlkit-0.12.0-py3-none-any.whl (37 kB)\n",
      "Requirement already satisfied: numpy~=1.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (1.21.5)\n",
      "Requirement already satisfied: jinja2<4.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (2.11.3)\n",
      "Collecting aiofiles<24.0,>=22.0\n",
      "  Downloading aiofiles-23.2.1-py3-none-any.whl (15 kB)\n",
      "Collecting orjson~=3.0\n",
      "  Downloading orjson-3.9.10-cp39-cp39-macosx_10_15_x86_64.macosx_11_0_arm64.macosx_10_15_universal2.whl (241 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m241.7/241.7 kB\u001b[0m \u001b[31m5.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: typing-extensions~=4.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (4.3.0)\n",
      "Collecting ffmpy\n",
      "  Downloading ffmpy-0.3.1.tar.gz (5.5 kB)\n",
      "  Preparing metadata (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25hCollecting gradio-client==0.8.0\n",
      "  Downloading gradio_client-0.8.0-py3-none-any.whl (305 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m305.1/305.1 kB\u001b[0m \u001b[31m6.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: pyyaml<7.0,>=5.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (6.0)\n",
      "Collecting pydantic>=2.0\n",
      "  Downloading pydantic-2.5.3-py3-none-any.whl (381 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m381.9/381.9 kB\u001b[0m \u001b[31m6.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hCollecting httpx\n",
      "  Downloading httpx-0.26.0-py3-none-any.whl (75 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m75.9/75.9 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting fastapi\n",
      "  Downloading fastapi-0.108.0-py3-none-any.whl (92 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m92.0/92.0 kB\u001b[0m \u001b[31m2.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: pillow<11.0,>=8.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (9.2.0)\n",
      "Requirement already satisfied: matplotlib~=3.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (3.5.2)\n",
      "Collecting pydub\n",
      "  Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)\n",
      "Collecting semantic-version~=2.0\n",
      "  Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)\n",
      "Collecting typer[all]<1.0,>=0.9\n",
      "  Downloading typer-0.9.0-py3-none-any.whl (45 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m45.9/45.9 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting huggingface-hub>=0.19.3\n",
      "  Downloading huggingface_hub-0.20.2-py3-none-any.whl (330 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m330.3/330.3 kB\u001b[0m \u001b[31m6.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: fsspec in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio-client==0.8.0->gradio) (2022.7.1)\n",
      "Collecting websockets<12.0,>=10.0\n",
      "  Downloading websockets-11.0.3-cp39-cp39-macosx_10_9_x86_64.whl (120 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m121.0/121.0 kB\u001b[0m \u001b[31m3.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: jsonschema>=3.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from altair<6.0,>=4.2.0->gradio) (4.16.0)\n",
      "Requirement already satisfied: toolz in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from altair<6.0,>=4.2.0->gradio) (0.11.2)\n",
      "Requirement already satisfied: requests in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from huggingface-hub>=0.19.3->gradio) (2.28.1)\n",
      "Collecting fsspec\n",
      "  Downloading fsspec-2023.12.2-py3-none-any.whl (168 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m169.0/169.0 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: filelock in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from huggingface-hub>=0.19.3->gradio) (3.6.0)\n",
      "Requirement already satisfied: tqdm>=4.42.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from huggingface-hub>=0.19.3->gradio) (4.64.1)\n",
      "Requirement already satisfied: zipp>=3.1.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from importlib-resources<7.0,>=1.3->gradio) (3.8.0)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (2.8.2)\n",
      "Requirement already satisfied: cycler>=0.10 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (4.25.0)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (1.4.2)\n",
      "Requirement already satisfied: pyparsing>=2.2.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (3.0.9)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from pandas<3.0,>=1.0->gradio) (2022.1)\n",
      "Collecting typing-extensions~=4.0\n",
      "  Downloading typing_extensions-4.9.0-py3-none-any.whl (32 kB)\n",
      "Collecting annotated-types>=0.4.0\n",
      "  Downloading annotated_types-0.6.0-py3-none-any.whl (12 kB)\n",
      "Collecting pydantic-core==2.14.6\n",
      "  Downloading pydantic_core-2.14.6-cp39-cp39-macosx_10_7_x86_64.whl (1.9 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.9/1.9 MB\u001b[0m \u001b[31m10.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: click<9.0.0,>=7.1.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from typer[all]<1.0,>=0.9->gradio) (8.0.4)\n",
      "Collecting shellingham<2.0.0,>=1.3.0\n",
      "  Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)\n",
      "Requirement already satisfied: colorama<0.5.0,>=0.4.3 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from typer[all]<1.0,>=0.9->gradio) (0.4.5)\n",
      "Collecting rich<14.0.0,>=10.11.0\n",
      "  Downloading rich-13.7.0-py3-none-any.whl (240 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m240.6/240.6 kB\u001b[0m \u001b[31m5.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hCollecting h11>=0.8\n",
      "  Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m2.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting starlette<0.33.0,>=0.29.0\n",
      "  Downloading starlette-0.32.0.post1-py3-none-any.whl (70 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m70.0/70.0 kB\u001b[0m \u001b[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting httpcore==1.*\n",
      "  Downloading httpcore-1.0.2-py3-none-any.whl (76 kB)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m76.9/76.9 kB\u001b[0m \u001b[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: anyio in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (3.5.0)\n",
      "Requirement already satisfied: certifi in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (2022.9.24)\n",
      "Requirement already satisfied: sniffio in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (1.2.0)\n",
      "Requirement already satisfied: idna in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (3.3)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio) (0.18.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio) (21.4.0)\n",
      "Requirement already satisfied: six>=1.5 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from python-dateutil>=2.7->matplotlib~=3.0->gradio) (1.16.0)\n",
      "Collecting markdown-it-py>=2.2.0\n",
      "  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m87.5/87.5 kB\u001b[0m \u001b[31m3.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting pygments<3.0.0,>=2.13.0\n",
      "  Downloading pygments-2.17.2-py3-none-any.whl (1.2 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m8.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: charset-normalizer<3,>=2 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from requests->huggingface-hub>=0.19.3->gradio) (2.0.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from requests->huggingface-hub>=0.19.3->gradio) (1.26.11)\n",
      "Collecting mdurl~=0.1\n",
      "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Building wheels for collected packages: ffmpy\n",
      "  Building wheel for ffmpy (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for ffmpy: filename=ffmpy-0.3.1-py3-none-any.whl size=5579 sha256=4423f5f66ab586eac216ee6878f8576bd402bb8a5b4cd2881db4eae5caa02b21\n",
      "  Stored in directory: /Users/mariaashby/Library/Caches/pip/wheels/1f/f1/8d/367922b023b526b7c2ced5db30932def7b18cf39d7ac6e8572\n",
      "Successfully built ffmpy\n",
      "Installing collected packages: pydub, ffmpy, websockets, typing-extensions, tomlkit, shellingham, semantic-version, python-multipart, pygments, orjson, mdurl, h11, fsspec, annotated-types, aiofiles, uvicorn, typer, starlette, pydantic-core, markdown-it-py, huggingface-hub, httpcore, rich, pydantic, httpx, altair, gradio-client, fastapi, gradio\n",
      "  Attempting uninstall: typing-extensions\n",
      "    Found existing installation: typing_extensions 4.3.0\n",
      "    Uninstalling typing_extensions-4.3.0:\n",
      "      Successfully uninstalled typing_extensions-4.3.0\n",
      "  Attempting uninstall: tomlkit\n",
      "    Found existing installation: tomlkit 0.11.1\n",
      "    Uninstalling tomlkit-0.11.1:\n",
      "      Successfully uninstalled tomlkit-0.11.1\n",
      "  Attempting uninstall: pygments\n",
      "    Found existing installation: Pygments 2.11.2\n",
      "    Uninstalling Pygments-2.11.2:\n",
      "      Successfully uninstalled Pygments-2.11.2\n",
      "  Attempting uninstall: fsspec\n",
      "    Found existing installation: fsspec 2022.7.1\n",
      "    Uninstalling fsspec-2022.7.1:\n",
      "      Successfully uninstalled fsspec-2022.7.1\n",
      "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "spyder 5.3.3 requires pyqt5<5.16, which is not installed.\n",
      "spyder 5.3.3 requires pyqtwebengine<5.16, which is not installed.\u001b[0m\u001b[31m\n",
      "\u001b[0mSuccessfully installed aiofiles-23.2.1 altair-5.2.0 annotated-types-0.6.0 fastapi-0.108.0 ffmpy-0.3.1 fsspec-2023.12.2 gradio-4.13.0 gradio-client-0.8.0 h11-0.14.0 httpcore-1.0.2 httpx-0.26.0 huggingface-hub-0.20.2 markdown-it-py-3.0.0 mdurl-0.1.2 orjson-3.9.10 pydantic-2.5.3 pydantic-core-2.14.6 pydub-0.25.1 pygments-2.17.2 python-multipart-0.0.6 rich-13.7.0 semantic-version-2.10.0 shellingham-1.5.4 starlette-0.32.0.post1 tomlkit-0.12.0 typer-0.9.0 typing-extensions-4.9.0 uvicorn-0.25.0 websockets-11.0.3\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "#pip install gradio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4ac96ff4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on local URL:  http://127.0.0.1:7860\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "import gradio as gr\n",
    "\n",
    "def greet(name, intensity):\n",
    "    return \"Hello \" * intensity + name + \"!\"\n",
    "\n",
    "demo = gr.Interface(\n",
    "    fn=greet,\n",
    "    inputs=[\"text\", \"slider\"],\n",
    "    outputs=[\"text\"],\n",
    ")\n",
    "\n",
    "demo.launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6c35aad4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: google-generativeai in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (0.3.2)\n",
      "Requirement already satisfied: gradio in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (4.13.0)\n",
      "Requirement already satisfied: Pillow in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (9.2.0)\n",
      "Collecting Pillow\n",
      "  Downloading pillow-10.2.0-cp39-cp39-macosx_10_10_x86_64.whl (3.5 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.5/3.5 MB\u001b[0m \u001b[31m9.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: google-ai-generativelanguage==0.4.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (0.4.0)\n",
      "Requirement already satisfied: google-auth in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (2.26.0)\n",
      "Requirement already satisfied: protobuf in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (4.25.1)\n",
      "Requirement already satisfied: typing-extensions in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (4.9.0)\n",
      "Requirement already satisfied: tqdm in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (4.64.1)\n",
      "Requirement already satisfied: google-api-core in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (2.15.0)\n",
      "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-ai-generativelanguage==0.4.0->google-generativeai) (1.23.0)\n",
      "Requirement already satisfied: jinja2<4.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (2.11.3)\n",
      "Requirement already satisfied: semantic-version~=2.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (2.10.0)\n",
      "Requirement already satisfied: typer[all]<1.0,>=0.9 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.9.0)\n",
      "Requirement already satisfied: numpy~=1.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (1.21.5)\n",
      "Requirement already satisfied: tomlkit==0.12.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.12.0)\n",
      "Requirement already satisfied: aiofiles<24.0,>=22.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (23.2.1)\n",
      "Requirement already satisfied: packaging in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (21.3)\n",
      "Requirement already satisfied: markupsafe~=2.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (2.0.1)\n",
      "Requirement already satisfied: uvicorn>=0.14.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.25.0)\n",
      "Requirement already satisfied: pandas<3.0,>=1.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (1.4.4)\n",
      "Requirement already satisfied: ffmpy in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.3.1)\n",
      "Requirement already satisfied: huggingface-hub>=0.19.3 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.20.2)\n",
      "Requirement already satisfied: pyyaml<7.0,>=5.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (6.0)\n",
      "Requirement already satisfied: fastapi in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.108.0)\n",
      "Requirement already satisfied: pydantic>=2.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (2.5.3)\n",
      "Requirement already satisfied: httpx in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.26.0)\n",
      "Requirement already satisfied: orjson~=3.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (3.9.10)\n",
      "Requirement already satisfied: python-multipart in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.0.6)\n",
      "Requirement already satisfied: altair<6.0,>=4.2.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (5.2.0)\n",
      "Requirement already satisfied: matplotlib~=3.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (3.5.2)\n",
      "Requirement already satisfied: pydub in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.25.1)\n",
      "Requirement already satisfied: gradio-client==0.8.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio) (0.8.0)\n",
      "Requirement already satisfied: importlib-resources<7.0,>=1.3 in /Users/mariaashby/.local/lib/python3.9/site-packages (from gradio) (5.12.0)\n",
      "Requirement already satisfied: fsspec in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio-client==0.8.0->gradio) (2023.12.2)\n",
      "Requirement already satisfied: websockets<12.0,>=10.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from gradio-client==0.8.0->gradio) (11.0.3)\n",
      "Requirement already satisfied: toolz in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from altair<6.0,>=4.2.0->gradio) (0.11.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from altair<6.0,>=4.2.0->gradio) (4.16.0)\n",
      "Requirement already satisfied: requests in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from huggingface-hub>=0.19.3->gradio) (2.28.1)\n",
      "Requirement already satisfied: filelock in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from huggingface-hub>=0.19.3->gradio) (3.6.0)\n",
      "Requirement already satisfied: zipp>=3.1.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from importlib-resources<7.0,>=1.3->gradio) (3.8.0)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (1.4.2)\n",
      "Requirement already satisfied: cycler>=0.10 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (4.25.0)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (2.8.2)\n",
      "Requirement already satisfied: pyparsing>=2.2.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from matplotlib~=3.0->gradio) (3.0.9)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from pandas<3.0,>=1.0->gradio) (2022.1)\n",
      "Requirement already satisfied: pydantic-core==2.14.6 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from pydantic>=2.0->gradio) (2.14.6)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from pydantic>=2.0->gradio) (0.6.0)\n",
      "Requirement already satisfied: click<9.0.0,>=7.1.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from typer[all]<1.0,>=0.9->gradio) (8.0.4)\n",
      "Requirement already satisfied: colorama<0.5.0,>=0.4.3 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from typer[all]<1.0,>=0.9->gradio) (0.4.5)\n",
      "Requirement already satisfied: shellingham<2.0.0,>=1.3.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from typer[all]<1.0,>=0.9->gradio) (1.5.4)\n",
      "Requirement already satisfied: rich<14.0.0,>=10.11.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from typer[all]<1.0,>=0.9->gradio) (13.7.0)\n",
      "Requirement already satisfied: h11>=0.8 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from uvicorn>=0.14.0->gradio) (0.14.0)\n",
      "Requirement already satisfied: starlette<0.33.0,>=0.29.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from fastapi->gradio) (0.32.0.post1)\n",
      "Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-api-core->google-generativeai) (1.62.0)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-auth->google-generativeai) (0.2.8)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-auth->google-generativeai) (4.9)\n",
      "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-auth->google-generativeai) (5.3.2)\n",
      "Requirement already satisfied: anyio in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (3.5.0)\n",
      "Requirement already satisfied: idna in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (3.3)\n",
      "Requirement already satisfied: httpcore==1.* in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (1.0.2)\n",
      "Requirement already satisfied: sniffio in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (1.2.0)\n",
      "Requirement already satisfied: certifi in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from httpx->gradio) (2022.9.24)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: grpcio-status<2.0.dev0,>=1.33.2 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-api-core->google-generativeai) (1.60.0)\n",
      "Requirement already satisfied: grpcio<2.0dev,>=1.33.2 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from google-api-core->google-generativeai) (1.60.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio) (0.18.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from jsonschema>=3.0->altair<6.0,>=4.2.0->gradio) (21.4.0)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from pyasn1-modules>=0.2.1->google-auth->google-generativeai) (0.4.8)\n",
      "Requirement already satisfied: six>=1.5 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from python-dateutil>=2.7->matplotlib~=3.0->gradio) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from requests->huggingface-hub>=0.19.3->gradio) (2.0.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from requests->huggingface-hub>=0.19.3->gradio) (1.26.11)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from rich<14.0.0,>=10.11.0->typer[all]<1.0,>=0.9->gradio) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from rich<14.0.0,>=10.11.0->typer[all]<1.0,>=0.9->gradio) (2.17.2)\n",
      "Requirement already satisfied: mdurl~=0.1 in /Users/mariaashby/opt/anaconda3/lib/python3.9/site-packages (from markdown-it-py>=2.2.0->rich<14.0.0,>=10.11.0->typer[all]<1.0,>=0.9->gradio) (0.1.2)\n",
      "Installing collected packages: Pillow\n",
      "  Attempting uninstall: Pillow\n",
      "    Found existing installation: Pillow 9.2.0\n",
      "    Uninstalling Pillow-9.2.0:\n",
      "      Successfully uninstalled Pillow-9.2.0\n",
      "Successfully installed Pillow-10.2.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "pip install  -U google-generativeai gradio Pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "79a85b9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on local URL:  http://127.0.0.1:7861\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7861/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Keyboard interruption in main thread... closing server.\n"
     ]
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "import gradio as gr\n",
    "import base64\n",
    "\n",
    "# Image to Base 64 Converter\n",
    "def image_to_base64(image_path):\n",
    "    with open(image_path, 'rb') as img:\n",
    "        encoded_string = base64.b64encode(img.read())\n",
    "    return encoded_string.decode('utf-8')\n",
    "\n",
    "# Function that takes User Inputs and displays it on ChatUI\n",
    "def query_message(history,txt,img):\n",
    "    if not img:\n",
    "        history += [(txt,None)]\n",
    "        return history\n",
    "    base64 = image_to_base64(img)\n",
    "    data_url = f\"data:image/jpeg;base64,{base64}\"\n",
    "    history += [(f\"{txt} ![]({data_url})\", None)]\n",
    "\n",
    "# UI Code\n",
    "with gr.Blocks() as app:\n",
    "    with gr.Row():\n",
    "        image_box = gr.Image(type=\"filepath\")\n",
    "   \n",
    "        chatbot = gr.Chatbot(\n",
    "            scale = 2,\n",
    "            height=750\n",
    "        )\n",
    "    text_box = gr.Textbox(\n",
    "            placeholder=\"Enter text and press enter, or upload an image\",\n",
    "            container=False,\n",
    "        )\n",
    "\n",
    "\n",
    "    btn = gr.Button(\"Submit\")\n",
    "    clicked = btn.click(query_message,\n",
    "                        [chatbot,text_box,image_box],\n",
    "                        chatbot\n",
    "                        )\n",
    "app.queue()\n",
    "app.launch(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0d88c05e",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''import os\n",
    "import google.generativeai as genai\n",
    "\n",
    "# Create the Model\n",
    "txt_model = genai.GenerativeModel('gemini-pro')\n",
    "vis_model = genai.GenerativeModel('gemini-pro-vision')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "732f4cae",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "#defining a function that takes image and text input and then generates a response and returns the updated history \n",
    "def llm_response(history,text,img):\n",
    "    if not img:\n",
    "        response = txt_model.generate_content(text)\n",
    "        history += [(None,response.text)]\n",
    "        return history\n",
    "    else:\n",
    "        img = PIL.Image.open(img)\n",
    "        response = vis_model.generate_content([text,img])\n",
    "        history += [(None,response.text)]\n",
    "        return history"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1c186ce5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import PIL.Image\n",
    "from fastapi import FastAPI\n",
    "import gradio as gr\n",
    "import base64\n",
    "import time\n",
    "import os\n",
    "import google.generativeai as genai\n",
    "app = FastAPI()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9757a28f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "env: GOOGLE_API_KEY=AIzaSyCq7pN8yH7MBAYnLuM53disPOKZuf_mFUk\n"
     ]
    }
   ],
   "source": [
    "#set Google API key\n",
    "%set_env GOOGLE_API_KEY=AIzaSyCq7pN8yH7MBAYnLuM53disPOKZuf_mFUk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "19efdb5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the Model\n",
    "txt_model = genai.GenerativeModel('gemini-pro')\n",
    "vis_model = genai.GenerativeModel('gemini-pro-vision')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "dabae3cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Image to Base 64 Converter\n",
    "def image_to_base64(image_path):\n",
    "    with open(image_path, 'rb') as img:\n",
    "        encoded_string = base64.b64encode(img.read())\n",
    "    return encoded_string.decode('utf-8')\n",
    "\n",
    "# Function that takes User Inputs and displays it on ChatUI\n",
    "def query_message(history,txt,img):\n",
    "    if not img:\n",
    "        history += [(txt,None)]\n",
    "        return history\n",
    "    base64 = image_to_base64(img)\n",
    "    data_url = f\"data:image/jpeg;base64,{base64}\"\n",
    "    history += [(f\"{txt} ![]({data_url})\", None)]\n",
    "    return history\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f0743f28",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function that takes User Inputs, generates Response and displays on Chat UI\n",
    "def llm_response(history,text,img):\n",
    "    if not img:\n",
    "        response = txt_model.generate_content(text)\n",
    "        history += [(None,response.text)]\n",
    "        return history\n",
    "\n",
    "    else:\n",
    "        img = PIL.Image.open(img)\n",
    "        response = vis_model.generate_content([text,img])\n",
    "        history += [(None,response.text)]\n",
    "        return history\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb322680",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on local URL:  http://127.0.0.1:7863\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7863/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Interface Code\n",
    "with gr.Blocks() as app:\n",
    "    with gr.Row():\n",
    "        image_box = gr.Image(type=\"filepath\")\n",
    "    \n",
    "        chatbot = gr.Chatbot(\n",
    "            scale = 2,\n",
    "            height=750\n",
    "        )\n",
    "    text_box = gr.Textbox(\n",
    "            placeholder=\"Enter text and press enter, or upload an image\",\n",
    "            container=False,\n",
    "        )\n",
    "\n",
    "    btn = gr.Button(\"Submit\")\n",
    "    clicked = btn.click(query_message,\n",
    "                        [chatbot,text_box,image_box],\n",
    "                        chatbot\n",
    "                        ).then(llm_response,\n",
    "                                [chatbot,text_box,image_box],\n",
    "                                chatbot\n",
    "                                )\n",
    "\n",
    "app.queue()\n",
    "app.launch(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d08f5fc1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
