<!DOCTYPE HTML>
<html>
    <head>
        <title>Maths test</title>
    </head>
    <body>
        <h1>Here are some quick questions</h1>
        <form action="/questions" method="POST">
%for categorie in questions:
            <ul>
%for q in questions[categorie]:
                <li>{{q.question}}{{!q.ask()}}</li>
%end
            </ul>
%end
            <input type="submit">
        </form>
    </body>
</html>
