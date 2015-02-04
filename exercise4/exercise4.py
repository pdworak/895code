
# coding: utf-8

# In[1]:

pwd


# In[87]:

# store file name.
file_name = "pg1513.txt"

line_count = 0
total_word_count = 0
total_char_count = 0
word_dict={}
count_dict = 0

# open the file.
my_file = open( "pg1513.txt", "r")

# loop over lines in file.
for current_line in my_file:

    # count lines in file
    line_count += 1
    
    # split line into words
    word_list_by_line = current_line.split()
    
    #count words by line
    line_word_count = len(word_list_by_line)
    
    #count total words by incrementing line counts
    total_word_count += line_word_count
    
    #-- loop over words by line to count characters and create word dictionary with incremental count --#        
    for word in word_list_by_line:
        char_count = len(word)
        total_char_count += char_count
        clean_word = word.replace(".", "").replace(",", "").replace("!", "").replace(";", "").replace(":", "").replace("[", "").replace("]", "")
        
        #check if the cleaning of special characters works
        #print (word)
        #print (clean_word)
        
        if ( clean_word not in word_dict ):
          word_dict[clean_word] = 1
        else:
          word_dict[clean_word] +=1
          
    #-- END loop over words by line --#        
               
    #check what is happening during iterations
    if line_count == 3: 
        
        print (word_list_by_line)
        print (line_word_count)
        print (total_word_count)
        print (word_dict)
     
#-- END loop over lines of file --#
    
print "total lines: " + str(line_count)
print "total words: " + str(total_word_count )
print "total characters: " + str(total_char_count )

#output the list with words and count

for clean_word in sorted(word_dict, key=word_dict.get, reverse=True):
    print ("count of " + clean_word + " = " + str(word_dict[clean_word]))
    
    # does sum of counted words equal sum of all words
    count_dict += word_dict[clean_word]
    
    # print (word)
    # print (word_dict[word])

    # END = printing words and values
    
if count_dict == total_word_count:
    print (str(count_dict) + " = " + str(total_word_count)+"  Spot on!")
    
my_file.close()


# In[ ]:



