curl -L https://api.github.com/repos/bipoza/txapa-bot/zipball/0.0.1 > release.zip
cd bipoza-txapa-bot-*
mkdir ../txapa-bot
mv * ../txapa-bot
cd .. && rm -rf bipoza-txapa-bot-*
cd txapa-bot/
echo "Installing dependencies..."
source /venv/bin/activate
pip install -r requirements.txt
echo "Done!"