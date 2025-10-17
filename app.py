from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def check_parameter():
    """
    מטפל בבקשות GET לנתיב הבסיס.
    בודק אם פרמטר השאילתה 'param' קיים.
    מחזיר "OK" אם קיים, ו-"EROR" אם חסר.
    """
    # request.args הוא אובייקט דמוי מילון המכיל את פרמטרי השאילתה שנותחו.
    # .get('param') מחזיר את הערך של 'param' או None אם הוא לא קיים.
    if request.args.get('param') is not None:
        return "OK"
    else:
        return "EROR"

if __name__ == '__main__':
    # מריץ את האפליקציה (נגישה מקומית בכתובת http://127.0.0.1:5000/)
    app.run(debug=True)
