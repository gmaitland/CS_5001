POEM = "Intensive technologies croon.\n\nLocal bandits lesson.\n" \
       "Old notebooks emote.\nVideos intersect.\n" \
       "Early notebooks choreograph.\n\nAsynchronous modems search.\n" \
       "Local desktops deliver.\nInteractive videos skill.\n" \
       "Grain tablets clap.\nNew technologies cry.\n\n" \
       "Commercial kits chant.\nSublingual tablets exalt.\n"

DREAM = "If tax payers tell their tale.\n" \
        "Of heated victories against the tax man.\n" \
        "A meeting with others who file late.\n\n" \
        "There were many reasons to file early...\n" \
        "Remembering what H&R Block said: 'Leave it to us!'\n" \
        "Ford cars with ejection seats - is that a valid deduction?\n\n" \
        "Peas and carrots, please - you barely ate dinner.\n" \
        "Floors covered with peas - you couldn't eat them after all.\n" \
        "Flux capacitors were science fiction - go back in time!\n\n" \
        "Flow with this - the deadline is looming.\n" \
        "Trails of paper litter your office.\n Follow the bouncing ball.\n" \
        "Follow the rabbit.\n\n Full of ideas; you're distracted again.\n" \
        "Scoops of ice cream await, finish the task!\n" \
        "Alas, you'll need an extension.\n" \
        "Rise up, go to bed - it's January and only a bad tax dream."

def print_acrostic(acrostic):
    column = acrostic[1]
    text = acrostic[0]
    
    phrases = text.split('\n')
    print('Original Poem: \n')
    print(text)
    print('Acrostic:\n')
    
    for each in phrases:
        if len(each) > 0:
            print(each[column], end='')
        else:
            print(' ', end='')
    print('\n')
    
def main():
    acrostics = [[POEM, 0], [DREAM, 3]]
    for each in acrostics:
        print_acrostic(each)

    
main()
    
