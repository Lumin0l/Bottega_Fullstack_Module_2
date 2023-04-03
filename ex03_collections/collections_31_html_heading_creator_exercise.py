'''
we want an automatic heading generator in this style:

heading_generator('hi there', '3')
<h3>hi there</h3>
'''

# My solution.

def heading_generator(content, heading_type):
    print(f'<h{heading_type}>{content}</h{heading_type}>')


heading_generator('henloooo', 1)

# His Solution:

# He does the exact same but with return instead of print.
