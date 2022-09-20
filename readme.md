# Resume Website

---

## Models

### Personal  

- profile : image
- Name : Text
- position : Text
- zip : int
- Address : big text
- Phone : Text
- Email : Email
- Github : URL
- Linkdin : URL
- Other : URL

### Education

- Institute : text
- Degree : text
- Score : float
- Study :  domain
- Start : Date
- Graduation : Date

### Experience

- proof : Image
- Start : date
- End : date
- Description : big text
- Employer : Text
- job_title : text
- Location : text
- currently : BooleanField

### Skills

- Type : Choice field( Language, framework, Tools, Databases, Soft)
- Name : text

### Projects

- cover : image
- name : text
- description : big text
- link : url
- completed : date
- skillset : manytomany(skills)
- on_job : foreignkey(job)

### Certificate

- cover : image
- name : text
- description : big text
- link : url
- org : text

### Additional

- achievement : big text

---
## Apps

- intro (personal, education, additonal)
- professional (experience, skillset)
- projects (projects, certificaions)

