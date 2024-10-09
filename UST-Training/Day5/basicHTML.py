Content = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .container{
            width: 1400px;
            height: 100vh;
            background-color: blueviolet;
        }
        .square{
            width: 200px;
            height: 200px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="square blue">

        </div>
    </div>
</body>
</html>

"""

with open('marathon.html', 'w') as fp:
    fp.write(Content)