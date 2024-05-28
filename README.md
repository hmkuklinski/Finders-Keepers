# Finders-Keepers
Finders Keepers is a Flask application that utilizes the EXA API to generate suggestive content for users based on the search parameters.

![Screenshot](https://media.discordapp.net/attachments/812752321867153409/1244917279838441474/Screenshot_2024-05-28_031713.png?ex=6656db10&is=66558990&hm=0fac109092f468fd766577d09431fb43dc62f31b002d16d351282a4ab7a436bb&=&format=webp&quality=lossless&width=851&height=397)

The User Interface makes it easy for users to search for their favorite topics on various platforms - TikTok, Twitter/X, and Instagram.

## How to Use:
The user will first type in their desired search topic, followed by the number of searches they would like returned (with a maximum of 7). The user will then select one of the three search options and click the green search button to generate results.

![Screenshot](https://media.discordapp.net/attachments/812752321867153409/1244917280572309584/Screenshot_2024-05-28_031744.png?ex=6656db11&is=66558991&hm=45221decd3f41d6d93bec149215ded6bdd0bb1b1986be4326f3c181a0211f3a7&=&format=webp&quality=lossless&width=858&height=397)

Here is an example of a search that may be entered.

## Possible Results: TikTok
The TikTok results can display: suggested user profiles, a discovery tag, or a suggested video.

### User Profile Preview:
![Screenshot](https://media.discordapp.net/attachments/812752321867153409/1244917281150992434/Screenshot_2024-05-28_031834.png?ex=6656db11&is=66558991&hm=921aad08cb8768dd5bdfc4cf152fbe17e886c5891d897daac00187b72095bece&=&format=webp&quality=lossless&width=858&height=397)

### Discovery Tag Preview:
![Screenshot](https://media.discordapp.net/attachments/812752321867153409/1244917281654439956/Screenshot_2024-05-28_032119.png?ex=6656db11&is=66558991&hm=9373b16ac363c35eaf28ce8b95f3d88ceb727c25bde08db35dafac2da569e38d&=&format=webp&quality=lossless&width=853&height=397)

Due to embedding issues with TikTok discovery tags, the user will be prompted to click on the discover image to open the discover tag link in a separate window. Unfortunately no preview of the discovery tag will be shown.

### Video Preview:
![Screenshot](https://media.discordapp.net/attachments/812752321867153409/1244917282262618173/Screenshot_2024-05-28_032244.png?ex=6656db11&is=66558991&hm=96b613905d414ee73ff267c16e2af2450dcfa69d19556a541b7c84d41aee2396&=&format=webp&quality=lossless&width=858&height=397)

Note: the embedded video will automatically start once it is fully loaded.


## Possible Results: Twitter/X

### User Timeline Preview:
![Screenshot](https://media.discordapp.net/attachments/812752321867153409/1244917283797598208/Screenshot_2024-05-28_032844.png?ex=6656db11&is=66558991&hm=34cfd63f4631cbc5b63c34c9cda7b8a7dfad3be3bd48752eabd2bad7329223b8&=&format=webp&quality=lossless&width=855&height=397)

The user will be able to see the posts from an account using the scroll bar and click the user profile to open in another tab.

### User Post:
It will sometimes suggest a single tweet that it thinks the user might like. 


## Possible Results: Instagram
![Screenshot](https://media.discordapp.net/attachments/812752321867153409/1244917279267754045/Screenshot_2024-05-28_023720.png?ex=6656db10&is=66558990&hm=7b0056df65962c794a14724797be9b8859239f6513508587d5a112b2e4376a9a&=&format=webp&quality=lossless&width=847&height=397)

The instagram link will mainly suggest accounts for the users to follow. The user will be able to see a preview of the user's past posts.

### User Post:
It will sometimes suggest a single post that it thinks the user might like. 
