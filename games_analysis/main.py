import pandas as pd
import matplotlib.pyplot as plt 

df_main = pd.read_csv("game-ratings-by-release-dates.csv")

df_main("first_release_date")=pd.to_datetime(df_main["first_release_date"])

plt.scatter(df_main["first_release_date"], df_main["critic_rating_value,"], color = "blue", label = "Critic Ratings")

plt.scatter(df_main["first_release_date"], df_main["user_rating_value"], color = "red" , label = "User Ratings")

plt.legend(loc = "upper left")

plt.show()

bar_width = 0.4

df_main = pd.read_csv("game-ratings-by-top-10-genres.csv")

df_follow = df_main.groupby(["genre_name"])["follow_count"].sum().reset_index()

df_follow = df_follow.rename(columns = { "follow_count": "total_follows"})
df_hype = df_main.groupby(["genre_name"])["hype_count"].sum().reset_index()

df_hype = df.rename(columns = {"hype_count": "total_hype"})

plt.bar(df_follow.index - bar_width / 2, df_follow["total_follows"], color = "blue", label = "Number of Follows", width = bar_width)

plt.bar(df_hype.index + bar_width / 2, df_hype["total_hypes"], color = "red", label = "Number of Hypes", width = bar_width)

plt.xticks(df_follow.index, df_follow("genre_name"))

plt.legend(loc = ("upper left"))

plt.show

df_main = pd.read_csv("game-ratings-by-top-10-platforms.csv")

df_follow = df_main.groupby(["platform_name"])["follow_count"].sum().reset_index()

df_follow = df_follow.rename(columns = { "follow_count": "total_follows"})
df_hype = df_main.groupby(["platform_name"])["hype_count"].sum().reset_index()

df_hype = df.rename(columns = {"hype_count": "total_hype"})

plt.bar(df_follow.index - bar_width / 2, df_follow["total_follows"], color = "blue", label = "Number of Follows", width = bar_width)

plt.bar(df_hype.index + bar_width / 2, df_hype["total_hypes"], color = "red", label = "Number of Hypes", width = bar_width)

plt.xticks(df_follow.index, df_follow("platform_name"))

plt.legend(loc = ("upper left"))

plt.show