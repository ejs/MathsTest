<!DOCTYPE HTML>
<html>
    <head>
        <title>Maths test</title>
    </head>
    <body>
        <h1>Here are some quick questions</h1>
        <form action="/questions" method="POST">
            <ul>
%for id, question in questions.items():
                <li>{{question}}<input /></li>
%end
            </ul>
            <input type="submit">
        </form>
    </body>
</html>
