# Tutorial - Deploy TenyxChat-8x7B-v1 using Inferless

Check out [this tutorial](https://tutorials.inferless.com/deploy-TenyxChat-8x7B-v1-using-inferless) which will guide you through the process of deploying a TenyxChat-8x7B-v1 model using Inferless.

## TL;DR - Deploy  using Inferless:
- Deployment of Deploy TenyxChat-8x7B-v1 model using [bitsandbytes](https://github.com/TimDettmers/bitsandbytes).
- By using the huggingface bitsandbytes, you can expect an average latency of 8.23 sec, generating an average of 12.24 tokens/sec where each token took 82.35 ms and an average cold start time of 24.66 sec using an A100 GPU(80GB).
- Dependencies defined in inferless-runtime-config.yaml.
- GitHub/GitLab template creation with app.py and inferless-runtime-config.yaml.
- Model class in app.py with initialize, infer, and finalize functions.
- Custom runtime creation with necessary system and Python packages.
- Model import via GitHub with input/output parameters in JSON.
- Recommended GPU: NVIDIA A100 for optimal performance.
- Custom runtime selection in advanced configuration.
- Final review and deployment on the Inferless platform.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Create a Custom Runtime in Inferless
To access the custom runtime window in Inferless, simply navigate to the sidebar and click on the Create new Runtime button. A pop-up will appear.

Next, provide a suitable name for your custom runtime and proceed by uploading the **inferless-runtime-config.yaml** file given above. Finally, ensure you save your changes by clicking on the save button.

### Add Your Hugging Face Access Token
This model requires a Hugging Face access token for authentication. You can provide the token in the following ways:

- **Via the Platform UI**: Set the `HF_TOKEN` in the **Environment Variables** section.
- **Via the CLI**: Add the `HF_TOKEN` as an environment variable.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the `Add a custom model` button.

- Select `Github` as the method of upload from the Provider list and then select your Github Repository and the branch.
- Choose the type of machine, and specify the minimum and maximum number of replicas for deploying your model.
- Configure Custom Runtime ( If you have pip or apt packages), choose Volume, Secrets and set Environment variables like Inference Timeout / Container Concurrency / Scale Down Timeout
- Once you click “Continue,” click Deploy to start the model import process.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/git-custom-code/git--custom-code) for more information on model import.

## Curl Command
Following is an example of the curl command you can use to make inferences. You can find the exact curl command on the Model's API page in Inferless.
```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
    "inputs": [
      {
        "data": [
          "What is an AI?"
        ],
        "name": "prompt",
        "shape": [
          1
        ],
        "datatype": "BYTES"
      }
    ]
}'
```


---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in the inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the GPU by setting `self.pipe = None`.


For more information refer to the [Inferless docs](https://docs.inferless.com/).
