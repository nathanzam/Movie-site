from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def merchandise():
    s = [{
      "name": "Coco: The Junior Novelization (Disney/Pixar Coco)",
      "rating": 5.0,
      "price": 5.35,
      "description": "Coco: The Junior Novelization retells the whole exciting movie and features eight pages of full-color scenes in this paperback novel. Despite his family’s baffling generations-old ban on music, Miguel (voice of newcomer Anthony Gonzalez) dreams of becoming an accomplished musician like his idol, Ernesto de la Cruz (voice of Benjamin Bratt). Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead following a mysterious chain of events. Along the way, he meets charming trickster Hector (voice of Gael García Bernal), and together, they set off on an extraordinary journey to unlock the real story behind Miguel’s family history. Directed by Lee Unkrich (Toy Story 3), co-directed by Adrian Molina (story artist Monsters University), and produced by Darla K. Anderson (Toy Story 3), Disney/Pixar’s Coco opens in U.S. theaters on November 22, 2017.",
      "itemType": "Book",
      "images": "https://images-na.ssl-images-amazon.com/images/I/51qzDTtaPWL._SX338_BO1,204,203,200_.jpg"
      },{
      "name": "Funko Mystery Mini: Disney/Pixar-Coco (One Mysery Figure) Collectible",
      "rating": 0,
      "price": 8.49,
      "description": "Your favorite characters from Disney/Pixar, as stylized vinyl mystery MINIS from Funko! Stylized collectibles stand 3 inches tall, perfect for any Disney/Pixar fan! Collect and display all Disney/Pixar mystery MINIS!",
      "itemType": "Bobblehead",
      "images": "https://images-na.ssl-images-amazon.com/images/I/71UVvo8H3KL._SL1293_.jpg"
      },{
      "name": "Funko Pop! Disney #303 Disney/Pixar Coco Miguel",
      "rating": 5,
      "price": 10.99,
      "description": "3.75 Inch Vinyl Figure, Officially Licensed, Window Box Packaging",
      "itemType": "Bobblehead",
      "images": "https://images-na.ssl-images-amazon.com/images/I/51t%2BW6vXIBL._SL1000_.jpg"
      },{
      "name": "DISNEY PIXAR COCO SKULLECTABLES LAND OF DEAD 5 PACK",
      "rating": 0,
      "price": 27.00,
      "description": "Disney / Pixar Coco Skullectables Land of the Dead Figure Set",
      "itemType": "Bobbleheads",
      "images": "https://images-na.ssl-images-amazon.com/images/I/71-IDjqJh6L._SL1000_.jpg"
      },{
      "name": "Coco Coloring Book: Disney Pixar Coco Coloring Pages for Boys and Girls",
      "rating": 0,
      "price": 5.95,
      "description": "Coloring book on Disney Pixar Coco animation. Simple illustrations for young kids.",
      "itemType": "Coloring Book",
      "images": "https://images-na.ssl-images-amazon.com/images/I/618EH3pqRQL._SX385_BO1,204,203,200_.jpg"
      },{
      "name": "Justice League: The Art of the Film",
      "rating": 0,
      "price": 28.77,
      "description": "Inspired by Superman's selfless act, Batman and Wonder Woman work quickly to find and recruit a team of metahumans – Aquaman, Cyborg, and The Flash – to save the planet from an assault of catastrophic proportions. Packed with stunning concept art, sketches, costume detail, stills, and behind-the-scenes shots from the set, this book is an invaluable insight into the world of Justice League.",
      "itemType": "Book",
      "images": "https://images-na.ssl-images-amazon.com/images/I/61RHDeFAndL._SY445_BO1,204,203,200_.jpg"
      },{
      "name": "The Justice League (Movie) 2018 Wall Calendar",
      "rating": 5,
      "price": 9.37,
      "description": "Fueled by his restored faith in humanity, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy in the new movie The Justice League. Together, Batman and Wonder Woman work to form an unprecedented league of heroeswhich includes Aquaman, Cyborg, and The Flashbut it may already be too late. The 2018 The Justice League Calendar, printed on paper certified by the Forest Stewardship Council, includes the last four months of 2017 and plenty of space to write in your important engagements.",
      "itemType": "Calendar",
      "images": "https://images-na.ssl-images-amazon.com/images/I/61aVnFVKBaL._SY498_BO1,204,203,200_.jpg"
      },{
      "name": "DC Collectibles Justice League 7-Pack Action Figure Box Set",
      "rating": 4.4,
      "price": 74.99,
      "description": "Contains Justice League icons Superman, Batman, Wonder Woman, Green Lantern, The Flash, Aquaman and Cyborg, Figures are 7 inches high. Highly detailed. Multiple points of articulation. The Justice League team together in one box set",
      "itemType": "Toys",
      "images": "https://images-na.ssl-images-amazon.com/images/I/71YYUcZ0zpL._SL1500_.jpg"
      },{
      "name": "Hot Wheels Justice League Toy Vehicle, 5-Pack",
      "rating": 5,
      "price": 19.99,
      "description": "Hot Wheels and Justice League fans will love recreating Super Hero moments with this 5-pack of premium character cars that includes five members of the Justice League team from the new movie in one pack. Batman, Superman, Wonder Woman, Aquaman and Cyborg all feature unique decos and details themed to the Justice League movie and they are ready to save the day. The Cyborg character car features an exclusive “power-up” deco to help him take on the team’s foes!. The 1:64 scale exclusive character cars features unique decos and details themed to the Justice League movie. These premium character cars are an instant collection for Super Hero fans!",
      "itemType": "Toys",
      "images": "https://images-na.ssl-images-amazon.com/images/I/81T7tDWXErL._SL1500_.jpg"
      },{
      "name": "Warner Bros. Stacked Logos - Justice League Movie Adult T-Shirt",
      "rating": 0,
      "price": 20.95,
      "description": "Officially licensed Justice League Movie product, assembled in the USA. Cool Stacked Logos print featuring logos for Justice League heros The Flash, Batman, Wonder Woman, Aquaman, Superman, and Cyborg. 100% cotton. Black",
      "itemType": "Clothing",
      "images": "https://images-na.ssl-images-amazon.com/images/I/71-Z8D5HHQL._UX679_.jpg"
      },{
      "name": "Wonder Movie Tie-In Edition",
      "rating": 4.4,
      "price": 8.73,
      "description": "Over 6 million people have fallen in love with Wonder and Auggie Pullman, the ordinary boy with the extraordinary face, who inspired a movement to Choose Kind. This special movie tie-in edition features an eight-page full-color insert with photos from the film, a foreword by the director Stephen Chbosky, an afterword by R.J. Palacio, a behind-the-scenes look at the making of the movie with anecdotes from the cast and crew, and a family discussion guide.",
      "itemType": "Book",
      "images": "https://images-na.ssl-images-amazon.com/images/I/41sviHmeghL._SX334_BO1,204,203,200_.jpg"
      },{
      "name": "Choose Kind Journal: Do One Wonderful Thing Every Day (A Wonder Journal)",
      "rating": 5.0,
      "price": 11.69,
      "description": "With more than 6 million copies sold worldwide and over five years as a New York Times bestseller, Wonder has inspired countless readers to reflect on their actions and to Choose Kind. This journal prompts writers to reflect on ways they can actively be kind every day to the people in their lives and to themselves.. Filled with quotes from the book and questions that are both fun and insightful, this journal is the perfect gift for a Wonder fan and a great activity for parents to do with their kids.",
      "itemType": "Journals",
      "images": "https://images-na.ssl-images-amazon.com/images/I/41LFQ7NoSqL.jpg"
      },{
      "name": "Wonder Wall Calendar 2018",
      "rating": 5,
      "price": 10.99,
      "description": "Choose kind, every day. The official Wonder Calendar captures the generous spirit of R. J. Palacio’s bestselling Wonder, with 17 months of inspiring quotes and words of wisdom, all illustrated in gorgeous full color. Each quote relates to the monthly theme, from Altruism to Self-reliance, and there is a corresponding activity that will spur action and conversation. The Wonder Calendar is a motivating meditation on kindness for the family or the classroom. This 17-month calendar starts in August 2017, in time for the new school year.",
      "itemType": "Calendar",
      "images": "https://images-na.ssl-images-amazon.com/images/I/61Xv52Mem%2BL._SY498_BO1,204,203,200_.jpg"
      },{
      "name": "Raymond Geddes & Company, Inc. Wonder Square Eraser 48/Box (70409)",
      "rating": 0,
      "price": 10.00,
      "description": ["8 designs featuring Auggie, Daisy, Summer and more!. 1 1/4 inch square, 1 /4inch thick. Quantity: 48 per box"],
      "itemType": "Erasers",
      "images": "https://images-na.ssl-images-amazon.com/images/I/61vf85acM5L._SL1000_.jpg"
      },{
      "name": "Four Wonder Notebooks: Draw, Dream, Doodle, and Write ",
      "rating": 0,
      "price": 10.17,
      "description": "With more than 6 million copies sold worldwide  and over fiveyears as a New York Times bestseller, Wonder has inspired countless readers to reflect on their actions and to Choose Kind. These notebooks--one lined, one blank, one bulleted, and one graph--are a colorful gift for Wonder fans, a useful back-to-school purchase, and colorful merchandise that can be traded among friends. With one blue, one red, one yellow, and one green cover, these notebooks will appeal to Wonder fans of both genders.",
      "itemType": "Journals",
      "images": "https://images-na.ssl-images-amazon.com/images/I/41fYumupWVL.jpg"
      },{
      "name": "Marvel's Thor: Ragnarok - The Art of the Movie",
      "rating": 5,
      "price": 45.00,
      "description": "Get an exclusive look at the art and designs behind the Mighty Avenger's newest fi lm in this latest installment of the popular ART OF series of movie tie-in books! A new all-powerful being threatens the destruction of Asgard, but Thor is trapped on the other side of the universe and must race against time to save his civilization. Go behind the scenes with exclusive concept artwork and in-depth analysis from the filmmakers in this keepsake volume!. Continuing their popular Art Of series of movie tie-in books, Marvel presents its latest blockbuster achievement! Featuring exclusive concept artwork, behind-the-scenes photographs, production stills, and in-depth interviews with the cast and crew, this deluxe volume provides insider details about the making of the highly anticipated film.",
      "itemType": "Book",
      "images": "https://images-na.ssl-images-amazon.com/images/I/51Sbl20dygL._SY406_BO1,204,203,200_.jpg"
      },{
      "name": "Thor: Ragnarok Official 2018 Calendar - Square Wall Format",
      "rating": 5,
      "price": 18.77,
      "description": "Danilo Promotions Limited (September 1, 2017) 2018 Wall calendar featuring incredible images from Marvel's Thor Ragnarok",
      "itemType": "Calendar",
      "images": "https://images-na.ssl-images-amazon.com/images/I/61ASwB9-XYL._SY498_BO1,204,203,200_.jpg"
      },{
      "name": "Pop! Marvel: Thor Ragnarok - Thor Gladiator Suit",
      "rating": 4.5,
      "price": 8.49,
      "description": "From Thor Ragnarok, Thor in Gladiator Suit, as a stylized pop vinyl from Funko!. Stylized collectible stands 3 ¾ inches tall, perfect for any Thor Ragnarok fan!. Collect and display all Thor Ragnarok pop! Vinyls!",
      "itemType": "Bobblehead",
      "images": "https://images-na.ssl-images-amazon.com/images/I/41rIz28IBoL.jpg"
      },{
      "name": "Pop! Marvel: Thor Ragnarok - Hulk Helmeted Gladiator",
      "rating": 4.5,
      "price": 8.78,
      "description": "From Thor Ragnarok, Hulk (helmeted gladiator), as a stylized pop vinyl from Funko!. Stylized collectible stands 3 ¾ inches tall, perfect for any Thor Ragnarok fan!. Collect and display all Thor Ragnarok pop! Vinyls!",
      "itemType": "Bobblehead",
      "images": "https://images-na.ssl-images-amazon.com/images/I/713NFlp87nL._SL1239_.jpg"
      },{
      "name": "Pop! Marvel: Thor Ragnarok - Hela Masked",
      "rating": 4.3,
      "price": 9.99,
      "description": "From Thor Ragnarok, Hela (masked), as a stylized pop vinyl from Funko!. Stylized collectible stands 3 ¾ inches tall, perfect for any Thor Ragnarok fan!. Collect and display all Thor Ragnarok pop! Vinyls!",
      "itemType": "Bobblehead",
      "images": "https://images-na.ssl-images-amazon.com/images/I/51owDOAsAzL.jpg"
      },{
      "name": "DADDY'S HOME 2 MOVIE POSTER 2 Sided ORIGINAL Advance 27x40 WILL FERRELL MARK WAHLBERG",
      "rating": 0,
      "price": 9.50,
      "description": "This is an Original Poster issued by the studio. It measures 27x40 inches. It is a double sided 1 Sheet. This poster is a great collectors item",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/715R38HsmFL._SL1113_.jpg"
      },{
      "name": "KANE HODDER Signed Hockey Mask Jason Voorhees Friday the 13th",
      "rating": 5.0,
      "price": 99.00,
      "description": "Kane Hodder Jason Voorhees in Friday the 13th Part 7,8,9,&10 Hand Signed Hockey Mask (Plastic) Kane added the inscription 'JASON 7,8,9,X' Autographed by Kane at our private signing. Comes with HorrorAutographs.com Authenticated Hologram on the item and HorrorAutographs.com Certificate of Authenticity (COA) also Comes with Photo of Kane Signing masks for us!",
      "itemType": "Mask",
      "images": "https://images-na.ssl-images-amazon.com/images/I/81k1KiUbfAL._SL1500_.jpg"
      },{
      "name": "Jaws Movie Memorabilia Jaws Film Cells Framed",
      "rating": 4.5,
      "price": 44.99,
      "description": "Features a pre-printed copy of an original cast signed Jaws image. Mounted with original Jaws movie film footage and engraved, numbered plaque. Housed in a custom made black frame. Certificate attached to the rear. Fantastic piece of Jaws memorabilia",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/51gyYYuzDCL.jpg"
      },{
      "name": "Goodfellas Signed + Goodfellas Film Cells Framed by artcandi",
      "rating": 3.5,
      "price": 44.99,
      "description": "Features a reproduction of an original cast signed Goodfellas promotional image. Mounted with original Goodfellas film footage & engraved, numbered plaque. Limited edition of only 700 worldwide. Certificate of authenticity attached to the rear. Perfect gift for any gangster movie fan",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/81b0bAgdmpL._SL1500_.jpg"
      },{
      "name": "Alien Movie Poster 11x17 Master Print",
      "rating": 4.1,
      "price": 8.98,
      "description": "For the best quality and fastest shipping, be sure to purchase from high feedback sellers.. Paper measures 11 inches x17 inches. (Chinese/Foreign seller versions are collages/mosaics from low-res images). (Not pillow cases, polyester flags, or plastic banners.). Ships rolled inside thick cardboard shipping/storage tube. No surprise customs fees or delays from Zero Feedback International sellers.",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/41VReP3cJoL.jpg"
      },{
      "name": "Star Wars The Force Awakens Movie Theater Exclusive 130oz Metal Popcorn Tub #4",
      "rating": 5.0,
      "price": 4.99,
      "description": "This is one of four different 130 oz metal embossed popcorn tubs from Star Wars The Force Awakens.",
      "itemType": "Collectible Bowl",
      "images": "https://images-na.ssl-images-amazon.com/images/I/91egHdgs-jL._SL1500_.jpg"
      },{
      "name": "George A Romero Signed / Autographed Night Of The Living Dead Movie Poster 8x10 Glossy Photo. Includes FANEXPO Certificate of Authenticity and Proof. Entertainment Autograph Original.",
      "rating": 4.5,
      "price": 129.99,
      "description": "George A Romero Signed Night Of The Living Dead Movie Poster Glossy Photo. This is not a movie poster in itself, but rather a 8x10 glossy photo of the movie poster signed by Romero. This from Starleaguesports include a genuine certificate of authenticity from Hobby Star Marketing with authentic hologram!",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/91rvW%2B72ALL._SL1500_.jpg"
      },{
      "name": "TONY MORAN Signed Steel Chef Knife Michael Myers Halloween I",
      "rating": 5.0,
      "price": 79.00,
      "description": "TONY MORAN 'Michael Myers in Halloween' Hand Signed Steel Chefs Knife (Approx 8-9 inches) Autographed by Tony at our signing in August 2016 Comes with HorrorAutographs.com Authenticated Hologram on the item and HorrorAutographs.com Certificate of Authenticity (COA) also Comes with Photo of Tony Signing Knives for us!",
      "itemType": "Collectible Knife",
      "images": "https://images-na.ssl-images-amazon.com/images/I/91GLatnuLlL._SL1500_.jpg"
      },{
      "name": "ALIENS MOVIE SCRIPT W/ REPRODUCTION SIGNATURES WEAVER, BIEHN, & HENN C3",
      "rating": 0,
      "price": 34.95,
      "description": "Reproduction script of Aliens starring Sigourney Weaver and directed by James Cameron, printed on heavy cardstock with reproductions of the signatures of the cast",
      "itemType": "Collectible Movie Script",
      "images": "https://images-na.ssl-images-amazon.com/images/I/71b5k15eM-L._SL1500_.jpg"
      },{
      "name": "Shawshank Redemption Movie Art Print — Movie Memorabilia — 11x17 Poster, Vibrant Color, Features Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler, Clancy Brown, Gil Bellows, James Whitmore.",
      "rating": 5.0,
      "price": 14.89,
      "description": "Shawshank Redemption illustrated Movie prints are highly-collectible pieces. With vibrant color, this beautiful poster is printed on Acid-Free Recycled paper with 30% post-consumer waste, as good stewards of the environment and with memorabilia preserving characteristics.",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/8161lfBoPJL._SL1482_.jpg"
      },{
      "name": "Collectibles Stamps - Superman Marvel DC Comics Movie MNH Stamp sheetlet 2016",
      "rating": 0,
      "price": 5.25,
      "description": "Stamp set featuring images from the classic Superman movie. Superman in different poses.. Perfect for fans of the Christopher Reeves classic.. High quality item professionally packaged with backing card, cello wrap and hard backed envelope. Sent within 24 hours",
      "itemType": "Poster stamps",
      "images": "https://images-na.ssl-images-amazon.com/images/I/91DBIfn6r0L._SL1500_.jpg"
      },{
      "name": "Friday the 13th Camp Crystal Lake Iron-on/Sew-on Embroidered PATCH",
      "rating": 5.0,
      "price": 5.25,
      "description": "FRIDAY the 13th CAMP CRYSTAL LAKE Logo EMBROIDERED PATCH. Embroidered patch features the Friday the 13th Camp Crystal Lake Sign. Patch measures 3 in. wide x 3 in. Tall. Can be ironed or sewn on",
      "itemType": "Clothing",
      "images": "https://images-na.ssl-images-amazon.com/images/I/81fy8N8TwoL._SL1263_.jpg"
      },{
      "name": "Limited Edition Glow-in-the-dark Horror Movie Killers Hannibal 0, Pinhead, Chucky, Leatherface, Scream and more Clock",
      "rating": 2.9,
      "price": 49.99,
      "description": "10.5 inches bt 10.5 inches. All your favorite movie killers. Eerily Glows After You Turn Out The Lights",
      "itemType": "Collectible Clock",
      "images": "https://images-na.ssl-images-amazon.com/images/I/818pMyRSUTL._SL1200_.jpg"
      },{
      "name": "Aliens Cast Autographed CGC Signature Series 9.8 Autograph Aliens #4 Comic Variant Cover",
      "rating": 0,
      "price": 1749.99,
      "description": "Personally hand signed by Sigourney Weaver, Bill Paxton, Paul Reiser, Lance Henriksen, William Hope, Michael Biehn, Carrie Henn, Ricco Ross, Daniel Kash, Cynthia Scott, Jenette Goldstein and Mark Rolston; In stock and ready to ship.. Includes Celebrity Authentics Certificates of Authenticity featuring a picture of each signing comic.. Certified by Celebrity Authentics, the world's leading source for genuine celebrity autographed memorabilia with every signature being personally witnessed by a Celebrity Authentics representative, cataloged into our on-line database (providing signing date, location and picture of the talent signing the item). It is then affixed with its own unique, serial-numbered authentication hologram that guarantees the item for life.. Certificate of Authenticity is included with every item, featuring a picture of the talent signing.",
      "itemType": "Collectible Comic Book",
      "images": "https://images-na.ssl-images-amazon.com/images/I/51O6wKpKxqL.jpg"
      },{
      "name": "Overlook hotel shirt funny graphic movie tshirts funny tees scary movie memorabilia graphic tee",
      "rating": 5.0,
      "price": 16.99,
      "description": "100% cotton. We stand behind our products. If you have any issues with your order please contact us and we will issue a refund, or replace your product free of charge.. We have something for everyone. Check out our entire collection ranging from Car and racing tshirts, to funny Dungeons and Dragons and gaming tshirts.. Preshrunk 4.2 oz ring-spun Guerrilla Tees® brand shirts",
      "itemType": "Clothing",
      "images": "https://images-na.ssl-images-amazon.com/images/I/61sGIfegTqL._UX679_.jpg"
      },{
      "name": "MasterPieces John Wayne Remembering the Duke Collage 1000 Piece Jigsaw Puzzle",
      "rating": 4.2,
      "price": 14.95,
      "description": "Collage of John Wayne images & memorabilia puzzle, 1000 pieces in finished 19.25 inch x 26.75 inch puzzle",
      "itemType": "Poster Puzzle",
      "images": "https://images-na.ssl-images-amazon.com/images/I/81Jk1kNnD7L._SL1088_.jpg"
      },{
      "name": "Star Wars The Force Awakens 12x18 reprint cast signed autographed movie poster #2",
      "rating": 0,
      "price": 19.99,
      "description": "The original photo has been reproduced onto Professional Glossy or Matte 12x18 inch poster photo paper with excellent color and image quality that will last a lifetime. 'Do Not Copy' will not be on the photo you receive. Signers include: Daisy Ridley, John Boyega, Harrison Ford, Mark Hamill and Carrie Fisher.",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/91tzvn2mRgL._SL1500_.jpg"
      },{
      "name": "Stephen King's IT - 12.5in. x17in. Original Promo Movie Poster Cinemark Pennywise",
      "rating": 5.0,
      "price": 40.00,
      "description": "This is a mini original promotional movie poster for the movie IT (2017). Poster measures approximately 12.5 inches x 19 inches and is in Mint Condition. Poster was exclusive to the Cinemark Theater Chain.",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/71wkFbQnUZL._SL1500_.jpg"
      },{
      "name": "Shawshank Redemption, Limited Edition Gold 45 Record Display",
      "rating": 0,
      "price": 84.95,
      "description": "Limited edition Shawshank Redemption movie poster and golden 45 record plaque.",
      "itemType": "Collectible Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/91kj5he9kRL._SL1500_.jpg"
      },{
      "name": "Rita Hayworth Poster 8.5x11 Photo, Shawshank Redemption",
      "rating": 0,
      "price": 11.99,
      "description": "The Beautiful Hollywood Actress RITA HAYWORTH. Also Know as The Famous Poster Hung In Andy's Cell In the Shaw-Shank Redemption. Professional High Quality 8.5x11 Image on Heavy-Weight Glossy Photo Stock",
      "itemType": "Poster",
      "images": "https://images-na.ssl-images-amazon.com/images/I/61breacPvrL._SL1077_.jpg"
    }]
    return jsonify(s)
