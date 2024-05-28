DROP DATABASE IF EXISTS friends;
CREATE DATABASE IF NOT EXISTS friends;
USE friends;

DROP TABLE IF EXISTS episodes;
CREATE TABLE episodes (
  episode_id int(3) not null,
  title varchar(50) not null,
  actor_id int(2) not null,
  air_date int(4) not null,
  season int(2) not null,
  episode_num int(2) not null,
  PRIMARY KEY (episode_id)
) ;

INSERT INTO episodes VALUES
(1, 'The Pilot', 5, 1994, 1, 1),
(2, 'The One With the Blackout', 3, 1994, 1, 7),
(3, 'The One With the Monkey', 4, 1994, 1, 10),
(4, 'The One With All the Poker', 5, 1995, 1, 18),
(5, 'The One Where Ross Finds Out', 4, 1995, 2, 7),
(6, 'The One With the Prom Video', 2, 1996, 2, 1),
(7, 'The One With the Two Parties', 1, 1996, 2, 22), 
(8, 'The One With the Football', 5, 1996, 3, 9),
(9, 'The One With the Dollhouse', 3, 1997, 3, 20),
(10, 'The One With the Cat', 3, 1997, 4, 1),
(11, 'The One With the Worst Best Man Ever', 5, 1998, 4, 22), 
(12, 'The One With All the Kissing', 4, 1998, 5, 2),
(13, 'The One With the Girl Who Hits Joey', 5, 1999, 5, 15),
(14, 'The One With the Apothecary Table', 3, 2000, 6, 11), 
(15, 'The One With Unagi', 4, 2000, 6, 17), 
(16, 'The One With the Truth About London', 1, 2001, 7, 16), 
(17, 'The One With the Vows', 10, 2001, 7, 21),
(18, 'The One With the Red Sweater', 1, 2001, 8, 1),
(19, 'The One With the Baby Shower', 1, 2002, 8, 20), 
(20, 'The One Where Monica Sings', 2, 2003, 9, 13),
(21, 'The One With the Mugging', 3, 2003, 9, 15), 
(22, 'The One After Joey and Rachel Kiss', 5, 2003, 10, 1),
(23, 'The One With the Cake', 2, 2003, 10, 4),
(24, 'The One With Princess Consuela', 3, 2004, 10, 14),
(25, 'The One With Rachels Going Away Party', 1, 2004, 10, 16);

DROP TABLE IF EXISTS characters;
CREATE TABLE characters (
  char_id int(2) not null,
  char_name varchar(50) not null,
  gender varchar(50) not null,
  age int(2) not null,
  apartment_id int(4) not null,
  PRIMARY KEY (char_id)
) ;

INSERT INTO characters VALUES
(1, 'Rachel Green', 'Female', 24, 1),
(2, 'Monica Geller', 'Female', 26, 1), 
(3, 'Phoebe Buffay', 'Female', 27, 3), 
(4, 'Ross Geller', 'Male', 26, 5), 
(5, 'Joey Tribbiani', 'Male', 27, 4), 
(6, 'Chandler Bing', 'Male', 27, 4),
(7, 'Gunther', 'Male', 28, 10),
(8, 'Janice Hosenstein', 'Female', 26, 8),
(9, 'Mike Hannigan', 'Male', 28, 6),
(10, 'Emily Waltham', 'Female', 27, 9); 

DROP TABLE IF EXISTS apartments;
CREATE TABLE apartments (
  apartment_id int(2) not null,
  number int(5) not null,
  building_name varchar(50) not null,
  street_name varchar(50) not null,
  city varchar(50) not null,
  state varchar(50) not null,
  zipcode int(5) not null,
  PRIMARY KEY (apartment_id)
) ;

INSERT INTO apartments VALUES
(1, 20, 'West Village', 'Bedford St', 'New York', 'NY', 10014),
(2, 4, 'West Village', 'Grove St', 'New York', 'NY', 10014),
(3, 5, 'West Village', 'Grove St', 'New York', 'NY', 10014),
(4, 19, 'West Village', 'Bedford St', 'New York', 'NY', 10014),
(5, 495, 'West Village', 'Grove St', 'New York', 'NY', 10014),
(6, 90, 'West Village', 'Bedford St', 'New York', 'NY', 10014),
(7, 453, 'West Village', 'Broome St', 'New York', 'NY', 10012),
(8, 12, 'East Village', '5th St', 'New York', 'NY', 10003),
(9, 16, 'West Village', 'Morton St', 'New York', 'NY', 10014);

DROP TABLE IF EXISTS relationships;
CREATE TABLE relationships (
  char1_id int(2) not null,
  char2_id int(2) not null,
  type varchar(50) not null,
  FOREIGN KEY (char1_id) REFERENCES characters(char_id),
  FOREIGN KEY (char2_id) REFERENCES characters(char_id)
) ;

INSERT INTO relationships VALUES
(1, 2, 'roommates'),
(1, 3, 'friends'),
(1, 4, 'romatic'),
(1, 5, 'friends'), 
(1, 6, 'friends'),
(1, 7, 'hopeless'),
(2, 3, 'friends'),
(2, 4, 'siblings'),
(2, 5, 'friends'), 
(2, 6, 'romantic'),
(3, 4, 'friends'),
(3, 6, 'friends'),
(4, 5, 'friends'),
(5, 6, 'roommates'), 
(3, 9, 'romantic'), 
(4, 10, 'hopeless'), 
(3, 5, 'flirty'),
(4, 6, 'friends'), 
(9, 10, 'unknown'), 
(7, 9, 'unknown'),
(7, 8, 'unknown'),
(1, 10, 'awkward'), 
(2, 10, 'awkward'),
(7, 9, 'unknown');

DROP TABLE IF EXISTS quotes;
CREATE TABLE quotes (
  quote_id int(3) not null,
  episode_id int(3) not null,
  character_id int(2) not null,
  quote_text varchar(200) not null,
  PRIMARY KEY (quote_id),
  FOREIGN KEY (episode_id) REFERENCES episodes(episode_id),
  FOREIGN KEY (character_id) REFERENCES characters(char_id)
);

INSERT INTO quotes VALUES
(1, 1, 2, "Welcome to the real world. It sucks! You’re gonna love it."),
(2, 1, 2, "It's like all my life everybody keeps telling that I'm a shoe."),
(3, 3, 3, "That is so cruel! Why? Why would a parent name their child Bethel?"),
(4, 2, 6, 'If Jill Goodacre offers you gum, you take it. If she offers you mangled animal carcass, you take it.'),
(5, 2, 5, 'The big question is, does he like you? Because if he doesn’t like you, this is all a moo point.'),
(6, 3, 4, 'It’s just all downhill from here.'),
(7, 3, 4, 'If you’re going to call me names, I would prefer Ross, the Divorce Force. It’s just cooler.'),
(8, 8, 6, 'Yes, it was so sad when the guy stopped drawing the deer.'),
(9, 4, 2, 'If you don’t help me cook I’m going to take a bunch of those hot dogs and make a new appetiser called pigs in Ross.'),
(10, 5, 4, 'You’re over me? When were you... under me?'),
(11, 5, 2, 'It’s not that common, it doesn’t happen to every guy, and it IS a big deal!'),
(12, 6, 3, 'Come on Ross you’re a palaeontologist – dig a little deeper.'),
(13, 6, 6, 'Alright, I’m not so good with the advice. Can I interest you in a sarcastic comment?'),
(14, 7, 3, 'See? He’s her lobster.'),
(15, 7, 5, "That's right. I stepped up! She's my friend and she needed help. And if I have to, I'd pee on any one of you."),
(16, 8, 4, "I have to say, I'm impressed. I never thought I'd be friends with a guy who could throw a girl that far."),
(17, 8, 5, 'Alright, look. If we’re gonna get serious about this, I’m gonna need a code name.'),
(18, 9, 5, 'Could I BE wearing any more clothes?!'),
(19, 9, 3, 'Joey, you can’t just give up meat. It’s like giving up a part of your self.'),
(20, 10, 3, 'They don’t know that we know they know we know.'),
(21, 10, 1, "Well, maybe I don't need your money. Wait, wait, I said maybe!"),
(22, 12, 5, "Joey doesn't share food!"),
(23, 22, 4, 'Pivot!'), 
(24, 21, 2, "Seven!"), 
(25, 18, 4, "We were on a break!"),
(26, 14, 4, "Y’know, we should probably ask the doctor if she even knows how to deliver a baby that’s half-human, half-pure evil!"),
(27, 19, 3, "If you want to receive emails about my upcoming shows, please give me money so I can buy a computer."),
(28, 15, 3, "Smelly cat, smelly cat, what are they feeding you? Smelly cat, smelly cat, it’s not your fault."),
(29, 24, 1, "Ross! We broke up two years ago. You’ve been married since then. I think it’s OK that we see other people."),
(30, 16, 6, "Because, Phoebe, sometimes after you sleep with someone you have to kill a fish.");






