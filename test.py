import requests


contexts = [
    "Help my sister bury her children. My sister lost her three amazing babies yesterday. Nothing will make this better, it will never be okay. But please if you can find it in your heart to help relieve the financial burden of this tragedy, please donate. No one should have to go through this.",
    """This year, we've seen a record number of anti-LGBTQIA bills pass through state legislatures across the country, especially in red states like Indiana. One of the scariest for me as a writer, though, is HB 1447, a book banning bill , which makes it easier for books about queer and BIPOC folks to not only be challenged, but also makes it easier to criminalize teachers and librarians for keeping those books available to young people.

As a writer, I've been fortunate that I’ve gotten to do a lot of great work on one side of this issue, but now I'm ready to do some work on the other side. And that's why I'm excited to announce Loudmouth Books. Loudmouth Books is an independent bookstore in Indianapolis, IN dedicated to uplifting the work of marginalized authors and highlighting diverse stories.

In short: Banned books are our business.

Not only are we putting those books on our shelves, but at Loudmouth Books, we're also doing everything in our power to get them into the hands of young people who need them. Following in the tradition of our friends at Semicolon Chicago , every month we are going to have a Clear the Shelves initiative, which makes it possible for young people across the city to come in and grab a diverse title free of charge.

That's right. We’re not only selling books, we're giving books away. I want to keep these books in the hands of the people who need them the most, which is why we need your support. By donating what you can, not only are you assisting in getting Loudmouth off the ground by helping us get our beautiful space up and running, but it also pours into our take on the Clear the Shelves initiative.

Loudmouth isn't a children’s only bookstore, though. We cover books for readers of all ages. Loudmouth Books is general interest with a passion and a mission to center stories by and about marginalized people, because we're here and we're Hoosiers too—we always have been, and we always will be.

I know that having access to the stories that reflect our experiences can save lives because those stories saved my life, as both a reader and a writer. And making sure that the people who write those stories and the readers who need them always have a home will never stop being one of my life's greatest priorities. There are a lot of tools in our arsenal to fight the good fight against books that we love being removed from shelves, and Loudmouth Books is mine.

I hope you'll join me.

In community,
Leah J.
""",
    """Devastating Family House Fire. Hi, my name is Celia and I’m raising funds on behalf of the loss of my family’s home in Woodbridge, Ontario. On the morning of June 19th, my brother Adam was awoken from his sleep to a devastating house fire. Being home alone at the time, he barely made his way out while the entirety of the house burnt down.

We are eternally grateful that no human life was taken or harmed in the fire. But, it is with heavy hearts that we mourn the loss of our 3 precious cats who were loved so dearly. Especially after Adam’s brave attempt to rescue them himself.

My Mom, Karen, has operated her own business inside of her home studio over the last 10+ years. She has devoted her life to helping others and has welcomed clients through her doors with open arms. For those who know my Mom, can understand how much of her heart goes into her work and into her home.

Unfortunately, we were not able to retrieve or recover anything from the house. My family has lost a lifetime’s worth of belongings from furniture, clothing, appliances, and all sentimental items that held immense value to us.

At this time we would appreciate any financial support to cover basic necessities and to assist my Mom with paying bills to recover from this devastating loss.

Thank you to our family, friends, neighbours and kind strangers for your continued support and generosity during this difficult time.""",
    """Please Help Save Orcas Arts and Gifts!
Please help us save our family business!!!

Our family has been operating Orcas Arts and Gifts since the late 1980's on Orcas Island, WA. While we have been dedicated rental tenants for the duration, we have recently been notified that the property will be going up for sale within the next 30 days. We have the opportunity to purchase before it hits the market, but we were completely unprepared for this to happen NOW. The seller is selling due to unexpected financial circumstances of their own.

This leaves us in a very tough situation. It is just me, my mother and stepfather of 33 years, who are in their senior years, trying to figure a way through this. My mom started this business in the late 1980’s, and soon after fell in love with my longtime stepfather, Patrick. Together they have built and maintained a niche with what many might call The Best Gift Shop on Orcas Island. I grew up in the shop and came back after college to help my family run the shop through a few medical situations, one of which is ongoing. As self-employed small business owners they don’t have much of a retirement fund to fall back on. I want to do whatever I can to help ensure Orcas Arts and Gifts can stay put for awhile.

Orcas Arts and Gifts is one of the oldest family-owned businesses on the island. The gift shop is inside a beautiful building that started out as the original Post Office on Main Street in the heart of Eastsound, WA. For decades, we have been a favorite stop for visitors and a reliable source of gifts of all kinds for locals. Generations of families have crossed our threshold, with children of children from families who love to come see their "favorite shop ever" (we hear this a lot and it makes us smile every time). We make our own jewelry. We design and print many of our own apparel designs. Not only that, but we are one of the last providers of full jewelry repair services for the San Juan Islands, including custom designs.

As one of the last existing vestiges of soulful and funky “Orcas”, we still have a lot to offer. We have poured our entire souls into the business, and we love this community and want to stay! I have grown up and out of my childhood on this island, and as an adult I have enjoyed becoming more involved in the local community. My heart is here. But, the timeline is short for the option to purchase, as the owner wants the sale to happen quickly. We have spent the past month agonizing over this, exploring every single option available to us, and we cannot come up with the down payment on our own in time.

Asking for help is not easy for us. We've always been able to handle our own things, but this is a monster of a purchase for us at this time. We need your help to make this dream a reality before time runs out.

With such a short timeline, we have been unable to scrape together our own resources and build up the funds needed to make a commercial real estate purchase with 30% down. Every day has been a rollercoaster of emotions as we dive deep into another option and find we are unable to proceed down that path.

So this is it. Our last chance to gamble on our future to stay and we have less than 30 days. Since the beginning, we have given back where we can to our community in the form of donations and fundraisers. We never really expected to be in a similar situation of need, but here we are.

Our main plan is to purchase this property. That is Priority #1 but in the event that we run out of time we intend to use any and all funds raised in this fundraiser to relocate the shop elsewhere, whether that means moving into a commercially-leased space (whenever one is available) or purchasing property and developing a new space there.

And for those of you who have been following our story for awhile - I promise I will write that book. And thank you, so much, Grace Grantham for such beautiful photos of our family.""",
]

for context in contexts:
    # _context = context.split()[0:140]
    url = f"http://localhost:7860/sentiment?text='{context}'"
    res = requests.get(url)
    data = res.json()
    print(data)
    sentiment = "neutral"
    if "output" in data and data.get("output"):
        sentiment = data.get("output")[0].get("label")
    print(sentiment, context[0:50])
