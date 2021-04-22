# Steps to make a Gbox

1. **First,** you&#39;ll need to install a working distribution of Docker. We recommend that Windows natives install WSL distribution, and then download Docker following the instructions from [here](https://docs.docker.com/docker-for-windows/wsl/) .

2. **Download and run** GranatumX locally:

    * Run **source \lt& ( docker run --rm -it granatumx/scripts:1.0.0 gx.sh )** to pull scripts and aliases from the docker container.
  
    * If you are running GranatumX for the first time, run **gx init.sh** ;otherwise,run **gx run.sh** to run the webapp. This command will tail the webapp. Wait until it starts the server, which should take 2 minutes to complete. You can &quot;ctrl c&quot; out of it    without stopping the service, and you can run **gxtail** to monitor the progress at any time.

    * Go to **localhost:34567** in your web browser to see the pipeline up and running.
  
    * If you would like to run as a web service for others, you can install and run Apache and use a Proxy to the port, but be sure to increase ProxyTimeout for large files and install to root &quot;/&quot; for the web location.

3. **Modify the template to install required dependencies.** Edit the Dockerfile by adding any package installation scripts your Gbox requires. You may add the commands to install packages directly in Dockerfile, or, if you are using the R template, feel free to modify the install\_packages.R script instead.

4. **Specify the name and version of your Gbox:** supply the Gbox name as the first line of GBOX\_BASE\_NAME.txt file (this name should be lowercase), and its version as the first name of the VERSION.txt file. Those two values will replace {VER} and {GBOX} in package.yaml file.

5. **Customize the package.yaml file:** A key requirement of a GranatumX Gbox is the package.yaml file. In this file, you&#39;ll add descriptive information about your Gbox, information about the backend scripts your Gbox uses to perform its operations, and definitions for the frontend user interface of your Gbox. For a full description of all available fields, check out the [index.d.ts](https://github.com/granatumx/install-gbox/blob/master/types/index.d.ts) file. Two key fields are briefly described below.

    The &quot;endpoints&quot; field contains the logic which will connect a user&#39;s pipeline to your Gbox backend. In our template, the Gbox backend is a docker image, and the command to be executed when the user runs your Gbox (in Python template) is &quot;python ./main.py&quot;. You can look at the g\_packages folder maybe add a link here? Couldn&#39;t find this folder in the Github repo that was originally linked for examples of other backend configuration options.

    The &quot;frontend&quot; field contains the &quot;args&quot; section defining what HTML inputs to show the user (these serve as the arguments which will be passed to your Gbox), the &quot;imports&quot; section defining what types of inputs from other Gboxes your Gbox accepts, and the &quot;exports&quot; section defining the types your Gbox exports to other Gboxes. The &quot;injectInto&quot; line should be modified to include keywords used to access args/imports/exports from the main script, as specified in the template comments.

6. **Edit your main script** main.R / main.py with your application code. The template provided demonstrates how to handle import/export of data using granatum\_sdk.

7. **Running gstage** from inside the folder containing the Gbox template will create a staging image, which you can use to test your Gbox.

8. **Running** gx installGbox.sh[name of the Gbox] will create a staging Gbox that can be accessed from the local &quot;server&quot; at localhost:34567. You can then experiment with your Gbox as a part of GranatumX&#39;s pipeline.

9. **If needed, run additional tests** locally. The script test/test.sh runs local testing on the Gbox and

    can be customized as desired. In order to initiate tests, you would need to run

    **gxtest /var/granatum/steps/step\_id**

    where **step\_id** can be found from the url of the step associated to the Gbox in your local GranatumX pipeline. For instance, one might run

    **Gxtest /var/granatum/steps/3faf4e2f-5415-47b3-a5a2-7160ff729a68** for an example value of step\_id = **3faf4e2f-5415-47b3-a5a2-7160ff729a68**

    You may also need to adjust permissions by running **chmod a+rx test/test.sh**

    Then, simply run **gtest** to initiate the testing. After the test is complete, you may access the results from the &quot;runtest&quot; folder, which should appear in the directory containing your Gbox material.

    Once the testing is complete, you may run **gx removeGbox [gbox name]** to remove the staging image. Then, run **gbuild** to build the image corresponding to your Gbox and deploy the final version by running **gx installGbox.sh [name of gbox]**.

    The testing and deployment process is summarized by the following diagram.
    
![Issue](https://user-images.githubusercontent.com/31740043/115763643-ad0f6a80-a372-11eb-8122-c0b85905bdef.png)

