# Working Examples with Vercel Functions

Check the examples out at:
[functions.immdom.com](functions.immdom.com)

you can also fork this repo and set it up with Vercel.
_REMEMBER: These functions ain't gonna work unless you push 'em up to Vercel!_

## basics

### Read The F!cking Manual
You should read the (https://vercel.com/docs/serverless-functions/introduction)[Vercel general introduction]
before proceeding, as well as the docs for whatever language you fancy.

### /api is special
Basically, you're going to add a script to the /api folder in a Vercel project.
When you deploy, it will generate a Function as a Service endpoint at the file name's path.

Nesting is allowed, as you can see with these examples.
```
/api/hello.js -> https://<APP_URL>/api/hello
/api/js/basic -> https://<APP_URL>/api/js/basic
```


(https://vercel.com/docs/serverless-functions/supported-languages)[Official Runtimes] include Ruby, Golang, Javascript, and Python.
Definitely check out what formats your function must be in.

### List the Examples

**Javascript**

[Basic Example](functions.immdom.com/js/basic)

[Params Example](functions.immdom.com/js/param) <-- try more params with /js/param?basicThing=<insertMe>

[Use Files at Runtime Example](functions.immdom.com/js/files)

**Python**
[Basic Example](functions.immdom.com/python/basic)

[Params Example](functions.immdom.com/python/param) <-- this is different. it just prints a dict of params.

[Requests Example](functions.immdom.com/python/git?username=paulkarayan) <-- lookup github user details with ?username=<insertMe>

[Flask Example](https://functions.immdom.com/api?domain=google.com) <-- dns lookup on a domain.

# Caveats

These examples represent my (@paulkarayan) limited exploration of Vercel functions.
Please let me know what I might be missing or doing wrong.

The documentation provided by Vercel is generally good, but lacks working examples.
In particular, there is a lot of information that appears to be out of date from the Zeit or now.sh
while the grand vision seems to have been reigned in considerably.

Overall - these are still really useful and amazing tools that are well worth the effort to understand.

_IMPORTANT_
You should probably treat these functions as middleware, not as full-fledged services themselves.
For example, if you want to use Flask to do some simple post/preprocessing - that's perfect.
However, if you want to build anything more fully featured, you should do it in a proper API server
setup with Flask or other tech. Bonus: you'll not have to worry about lack of observability!

Also - Node.js is clearly the preferred choice here. I don't mind it but take a look at the
inability to use files with the Python example.

## What Doesn't Make Sense / Work

- I can't seem to get files to work with Python.

Vercel Discussion post [here](https://github.com/vercel/vercel/discussions/5083)

- can flask apps have multiple routes or entry points?

Vercel Discussion post [here](https://github.com/vercel/vercel/discussions/5084)
