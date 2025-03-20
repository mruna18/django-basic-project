from django.shortcuts import render
from base.models import ArticleData,NewsData,EventsData
# Create your views here.

# article_data=[
#   {
#     'id':1,
#     'title':'india',
#     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
#   },
#   {
#     'id':2,
#     'title':'germany',
#     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
#   },
#   {
#     'id':3,
#     'title':'south korea',
#     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
#   },
#   {
#     'id':4,
#     'title':'england',
#     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
#   },
#   {
#     'id':5,
#     'title':'canada',
#     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
#   },
# ]

article_data=ArticleData.objects.all()

def home(request):
    # print(all_data)
  return render(request,'home.html',{'home':article_data})

# def article_details(request,detail_id):
# #   article_details={
# #    1: {
# #     'id':1,
# #     'title':'india',
# #     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
# #   },
# #   2: {
# #     'id':2,
# #     'title':'germany',
# #     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
# #   },
# #   3: {
# #     'id':3,
# #     'title':'south korea',
# #     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
# #   },
# #   4: {
# #     'id':4,
# #     'title':'england',
# #     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
# #   },
# #   5: {
# #     'id':5,
# #     'title':'canada',
# #     'desc':"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum expedita iste vel reprehenderit quo nihil totam, officia inventore fuga maiores. Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, doloribus?"""
# #   },
# # }
#   # article = article_details.get(detail_id, None)
#   articleDetails=ArticleDetails.objects.all()
#   return render(request,'article_details.html',{'article':articleDetails})

def about(request):
  about="About the project: "
  return render(request,'about.html',{'about':about})


def read(request,pk):
  print(type(pk))
  for i in article_data:
    if i.id==pk:
      return render(request,'read.html',{'data':i})



# news_data= [
#     {
#       "id":1,
#         "title": "Tech Advances in 2025",
#         "author": "Mrunali P",
#         "date": "2025-02-22",
#         "content": "New AI models are revolutionizing industries, automating tasks that were once considered impossible. "
#                    "With advancements in machine learning, businesses are seeing increased efficiency and accuracy. "
#                    "Companies like OpenAI and Google are leading the charge with groundbreaking innovations in generative AI, "
#                    "creating tools that assist in writing, coding, and even complex problem-solving. As AI regulation debates continue, "
#                    "governments are working to establish guidelines to ensure ethical and responsible use of AI in various sectors."
#     },
#     {"id":2,
#         "title": "Stock Market Update",
#         "author": "Jin k",
#         "date": "2025-02-22",
#         "content": "The stock market saw a significant rise today as major tech companies reported strong earnings. "
#                    "The S&P 500 and NASDAQ both gained over 2%, fueled by investor confidence in the growing AI industry. "
#                    "Tesla and Apple were among the biggest gainers, with their stock prices surging due to positive quarterly results. "
#                    "Analysts predict continued volatility in the market as interest rate concerns persist, but optimism remains high "
#                    "for sectors such as AI, renewable energy, and healthcare technology."
#     },
#     {"id":3,
#         "title": "Sports Highlights",
#         "author": "Terry k",
#         "date": "2025-02-22",
#         "content": "The championship game ended in a thrilling victory as the underdog team secured a last-minute goal. "
#                    "Fans erupted in excitement as the final whistle confirmed their unexpected triumph. "
#                    "Star player Jake Thompson delivered a stunning performance, scoring twice and assisting the winning goal. "
#                    "The victory marks a historic moment for the team, who had struggled throughout the season. "
#                    "Experts believe this win will reshape the league’s competitive landscape for the coming years."
#     }
# ]

news_data=NewsData.objects.all()
def news(request):
 
  return render(request,'news.html',{'news_data':news_data})


def news_post(request,id):
  for news in news_data:
    if news.id==id:
      return render(request,'news_details.html',{'data_news':news})


# events_data=[
#   {
#     "id": 1,
#     "name": "Tech Conference",
#     "date": "2025-03-15",
#     "location": "San Francisco",
#     "type": "Technology"
#   },
#   {
#     "id": 2,
#     "name": "Music Festival",
#     "date": "2025-06-22",
#     "location": "New York",
#     "type": "Entertainment"
#   },
#   {
#     "id": 3,
#     "name": "Art Exhibition",
#     "date": "2025-04-10",
#     "location": "Paris",
#     "type": "Art"
#   },
#   {
#     "id": 4,
#     "name": "Hackathon",
#     "date": "2025-05-05",
#     "location": "Online",
#     "type": "Programming"
#   },
#   {
#     "id": 5,
#     "name": "Marathon",
#     "date": "2025-07-12",
#     "location": "Berlin",
#     "type": "Sports"
#   }
# ]

events_data = EventsData.objects.all()
def events(request):
  return render(request,'events.html',{'events_data':events_data})

def events_details(request,event_id):
  for i in events_data:
    if i.id==event_id:
      return render(request,'events_details.html',{'data_events':i})