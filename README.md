# Classwork on using the Django ORM capability from the console

## Exercise 1:
* Create new model for ```Author```
- Author should have properties for ```first_name``` and ```last_name```

* Create a new model for ```Post```
- Post should have properties for ```title```, ```content```, ```date_posted```, and ```author```
-- ```date_posted``` should automatically populate with current date on create
-- ```author``` should be a foreign key that points back to the Author of the post(s)


* Open the Django shell
- Import the models
- Create an instance of ```Author``` in the shell
- Create 3 posts associated with the author

Use the Django shell and the admin console to check that the records were created

From the shell copy the commands your entered in the shell to create the instances and the relationships AT THE BOTTOM OF THIS README.


============================

Copy the shell commands you used here!
>>> a1 = Author(first_name = "John", last_name = "White")

>>>> a1.save()
>
>>> p1 = Post(title = "My People", content = "100 Pages", author = a1)
>
>>> p1.save()
>
>>> p2 = Post(title = "Sleep", content = "152 Pages", author = a1)
>
>>> p2.save()
>
>>> p3 = Post(title = "Happy Song", content = "20 Pages", author = a1)
>
>>> p3.save()
>
>>>> a1.post_set.all()
>
>QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>]>


