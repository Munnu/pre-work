# -*- coding: utf-8 -*-

# A short story using conditionals and a loop 

your_character = raw_input("What's your name?: ")
friend = raw_input("What's the name of someone you'd like to go on an adventure with?: ")

print "\n"
print "Once, long ago, there was a woman who lived alone in the country"
print "with her children %s and %s." % (your_character, friend)
print "On the day of their grandmother's birthday, the good mother set off"
print "to see her, leaving the children at home."
print "Before she left, she said, \"Be good while I am away, my heart-loving"
print "children; I will not return tonight. Remember to close the door tight at"
print "sunset and latch it well.\""
print "But an old wolf lived nearby and saw the good mother leave. At dusk,"
print "disguised as an old woman, he came up to the house of the children"
print "and knocked on the door twice: bang, bang."
print "\n-------------------------------------------"
print "Maybe you can help them make a great decision!:"
print "Who should answer the door? Choose '1' for %s or choose '2' for %s." % \
		(your_character, friend)

person = int(raw_input("Who should answer? "))

if person == 1:
    print "\n%s, said through the latched door, \"Who was it?\"" % (your_character)

elif person == 2:
    print "\n%s, said through the latched door, \"Who was it?\"" % (friend)
else:
    print "Both children said through the latched door \"Who was it?\""

print "\"My little jewels\", said the wolf, \"this is your grandmother, your Po Po\"."
print "\"Po Po!\" %s said. \"Our mother has gone to visit you!\"" % (your_character)
print "The wolf acted surprised. \"To visit me? I have not met her along the way."
print "She must have taken a different route.\" \"Po Po!\" %s said." % (your_character)
print "\"How is it that you come so late?\" The wolf answered,"
print "\"The journey is long, my children, and the day is short.\""
print "%s listened through the door. \"Po Po,\" %s said," % (friend, friend)
print "\"why is your voice so low?\" \"Your grandmother has caught a cold,"
print "good children, and it is dark and windy out here."
print "Quickly open up, and let your Po Po come in,\" the cunning wolf said."

print "\n-------------------------------------------"
answer_door = int(raw_input("Do you want to answer the door? 1 for yes 2 for no "))

if answer_door == 1:
    print "\n"
    print "One unlatched the door and the other opened it."
    print "They shouted, \"Po Po, Po Po, come in!\""
    print "At the moment he entered the door, the wolf blew out the candle."
    print "\"Po Po,\" %s asked, \"why did you blow out the candle?" % (your_character)
    print "The room is now dark.\""
    print "The wolf did not answer."
    print "%s and %s rushed to their Po Po and wished to be hugged." % (your_character, friend)
    print "The old wolf held %s. \"Good child, you are so plump.\"" % (your_character)
    print "He embraced %s." % (friend)
    print "\"Good child, you have grown to be so sweet.\""
    print "Soon the old wolf pretended to be sleepy. He yawned."
    print "\"All the chicks are in the coop,\" he said. \"Po Po is sleepy too.\""
    print "\n"
    print "When he climbed into the big bed, %s climbed in at one end" % (your_character)
    print "with the wolf, and %s climbed in at the other." % (friend)
    print "But when %s stretched, she touched the wolf's tail." % (friend)
    print "\"Po Po, Po Po, your foot has a bush on it.\""
    print "\"Po Po has brought hemp strings to weave you a basket,\" the wolf said."
    print "%s touched grandmother's sharp claws." % (your_character)
    print "\"Po Po, Po Po, your hand has thorns on it.\""
    print "\"Po Po has brought an awl to make shoes for you,\" the wolf said."
    print "At once, %s lit the light and the wolf blew it out again," % (your_character)
    print "but %s had seen the wolf's hairy face." % (your_character)
    print "\n"
    print "\"Po Po, Po Po,\" %s said, being the most clever," % (your_character)
    print "\"you must be hungry. Have you eaten ginkgo nuts?\""
    print "\"What is ginkgo?\" the wolf asked."
    print "\"Ginkgo is soft and tender, like the skin of a baby."
    print "One taste and you will live forever,\" %s said," % (friend)
    print "\"and the nuts grow on the top of the tree just outside the door.\""
    print "The wolf gave a sigh. \"Oh, dear. Po Po is old, her bones have become brittle."
    print "No longer can she climb trees.\""
    print "\"Good Po Po, we can pick some for you,\" %s said." % (your_character)
    print "The wolf was delighted."
    print "%s jumped out of bed and %s came with her to the ginkgo tree." % (your_character, friend)
elif answer_door == 2:
    print "\n"
    print "The wolf began to bang on the door harder and harder"
    print "and begins to cry: \"My little grandchildren!\""
    print "Both children began to feel scared and ran to the window in the back,"
    print "worried that it was not their Po Po after all, they wanted to escape."
    print "\Po Po, Po Po,\" %s said, \"you must be hungry." % (your_character)
    print " Have you eaten ginkgo nuts?\""
    print "\"What is ginkgo?\" the wolf asked."
    print "\"Ginkgo is soft and tender, like the skin of a baby."
    print "One taste and you will live forever,\" %s said," % (friend)
    print "\"Give us a moment to open the door and give them to you\", the children said"
    print "The children ran outside from the back window, headed for the gingko"
    print "tree in the front of the yard. As they were running, they saw"
    print "a glimpse of what was not their Po Po, but rather a furry wolf!"
else:
    print "\n"
    print "I guess the story is too much for you!"

if answer_door == 1 or answer_door == 2:
    print "There, %s told %s about the wolf and both climbed up the tall tree." \
        % (your_character, friend)
    print "The Wolf waited and waited."
    print "Plump %s did not come back." % (your_character)
    print "%s did not come back, and no one brought any nuts from the gingko tree." % (friend)
    print "At last the wolf shouted, \"where are you, children?\""
    print "\"Po Po,\" %s called out, \"we are on the top of the tree eating gingko nuts.\"" % (friend)
    print "\"Good children,\" the wolf begged, \"pluck some for me.\""
    print "\"But Po Po, gingko is magic only when it is plucked directly from the tree."
    print "You must come and pluck it from the tree yourself.\"" 
    print "\n"
    print "The wolf came outside and paced back and forth under the tree where he"
    print "heard the three children eating the gingko nuts at the top."
    print "\"Oh, Po Po, these nuts are so tasty!  The skin so tender,\" %s said." % (friend)
    print "The wolf’s mouth began to water for a taste."
    print "Finally, %s, said, \"Po Po, Po Po, I have a plan." % (friend)
    print "At the door there is a big basket.  Behind it is a rope."
    print "Tie the rope to the basket, sit in the basket and throw the other end to me."
    print "I can pull you up.\""
    print "The wolf was overjoyed and fetched the basket and the rope,"
    print "then threw one end of the rope to the top of the tree."

    print "\n-------------------------------------------"
    num_of_pulls = int(raw_input("How many times should we try to rope the wolf up? "))
    print "The children caught the rope and began to pull the basket up the up.\n\n"

    for i in range (num_of_pulls):
        print "The children pulled the rope with all of their strength"
        print "and counted %d, and let go of the rope halfway." % (i+1)
        print "The wolf and the basket fell straight back down to the ground."
        print "\n"

    print "\nNot only did the wolf bump his head, but he broke his heart to pieces."
    print "\"Po Po,\" %s shouted, but there was no answer." % (your_character)
    print "\"Po Po,\" %s shouted, but there was no answer." % (friend)
    print "The children climbed to the branches just above the wolf and "
    print "saw that he was truly dead. Then they climbed down, went into the house,"
    print "closed the door, locked the door with the latch and fell peacefully asleep."
    print "On the next day, their mother returned with baskets of feed from their real"
    print "Po Po, and the three sisters told her the story of the Po Po who had come."
print "The end."
