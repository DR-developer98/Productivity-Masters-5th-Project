[logo]

# Productivity Masters
<p>Description of the application and its objectives</p>

## EPICS and User stories
<p>The structure and functioning of this application is based on the following EPICS:</p>

* First EPIC (name):
1. First user story
2. Second user story
3. Third user story

* Second EPIC (name):
1. First user story
2. Second user story
3. Third user story

* Third EPIC (name):
1. First user story
2. Second user story
3. Third user story

* Fourth EPIC (name):
1. First user story
2. Second user story
3. Third user story

<p>For the implementation of these user stories, I used the following project (<a href="#">ADD PROJECT</a>) as a backlog.</p>

## Wireframes

[Wireframes]

<p>Link to repository: <a href="https://github.com/DR-developer98/Productivity-Masters-5th-Project" target="_blank">Productivity-Masters-5th-Project</a></p>
<p>Link to deployed project: <a href="#" target="_blank">Add link</a></p>

## ERD

[ERD]

## Implementation of the EPICS/User Stories

### Categories
<p>When creating a new task, the user may decide not to assign a category to the new item.</p>

## Testing

<p>For the testing part, including fixed bugs, please refer to <a href="./TESTING.md">TESTING.md</a></p>

## Deployment

## Debugging

* While building the attachments app, upon trying to open a previously uploaded pdf file, I would get an error from 
Cloudinary, stating that it was impossible to open a pdf file. This was solved by doing the following:
<ol>
    <li>adding the folling code in settings.py:</li>
    <ul>
        <li> use_filename=True ensures that Cloudinary uses the original filename;</li>
        <li> unique_filename=False prevents Cloudinary from adding the randomly generated suffix;
        <img src="../images_for_README/cloudinary_settings_file_upload.PNG">
        </li>
    </ul>
    <li>adding the following code to the attachments>serializers.py:</li>
    <ul>
        <li>this establishes the allowed file extensions;</li>
        <li>checks whether the uploaded file has one of the allowed extensions;</li>
        <li>returns the file name if it has passed the validation system;</li>
        <li>returns this error message: _"Only PDF, TXT, DOC, and DOCX files are allowed."_ if the extension is not allowed.
        <img src="../images_for_README/attachment_serializer_file_validation.PNG"></li>
    </ul>
    <li>changing the security settings in my Cloudinary account:  
    <img src="../images_for_README/security_settings_cloudinary.PNG"></li>
</ol>

## Credits

### Content

* For the profile model, views and serializer I've referenced Code Institute's Django Rest Framework module;
* Stackoverflow:

### Used technologies and media

