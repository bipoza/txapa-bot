import schedule
import time
from datetime import datetime
from bot import new_podcast_sender

def main():

    def job():
        # print("I'm working...")
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(date)

    schedule.every().minute.do(job)
    schedule.every(10).minutes.do(new_podcast_sender)

    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)
    # schedule.every(5).to(10).minutes.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    # schedule.every().minute.at(":17").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()