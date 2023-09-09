# isec6000-assignment1-task1

## Create a cluster
- Go to google cloud console (https://console.cloud.google.com/) 
- Click on Kubernetes engine and then clusters, the following page will appear:

![Screenshot 2023-09-09 221336](https://github.com/jeanyego/isec6000-assignment1-task1/assets/44524100/b93f6931-5092-4e6e-85d2-f7f3200b29a5)

- Create a project ID using shell or you can fill the fields in the form.
  ![Screenshot 2023-09-09 221424](https://github.com/jeanyego/isec6000-assignment1-task1/assets/44524100/800ae9f6-ef90-441b-b779-d09e79dac878)

- ```gcloud config set project ISEC6000```
- You can manually create a cluster using the following command:
- ```gcloud container clusters create-auto assignment1\ --location =us-central1```
- The simpler way will be to follow the steps on the form and create the cluster.
- ![Screenshot 2023-09-09 221451](https://github.com/jeanyego/isec6000-assignment1-task1/assets/44524100/75bfdce3-bb69-4dcf-9ea9-9cb190ec6802)

- After a successful creation of the cluster you need to connect it to the kubernetes engine, you can do this with the following command: 
```gcloud container clusters get-credentials assignment1 --region us-central1 --project isec6000-396805```
Change the above to match your project ID and cluster name
![Screenshot 2023-09-09 221553](https://github.com/jeanyego/isec6000-assignment1-task1/assets/44524100/cfe6b75f-b730-44bf-8bb2-4281b44db673)
- When using shell you will need to authorise.
- The connection of our cluster to kubernetes engine completes a successfull creation.
