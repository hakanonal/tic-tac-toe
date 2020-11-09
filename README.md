# Tic-Tac-Toe

I have inspired this project from a conference called [IstanbulTechWeek](https://www.istanbultechweek.com) that has been held on-line in the begining of 2020 November. In the first day of this confenrence there was a very simple [explanation](https://youtu.be/aV7-4iKWOuw) of how to implement a reinforcement q-learning algorithm that implements tic-tac-toe. The presentation was made succesfully by [Joe Fitzgerald](https://www.linkedin.com/in/js-fitz/). I would like to thank him here for his contributions. I just wanted to bring my own solution here to see how I could quickly do that. 

## Journal

#### 08.11.2020

- Created the repository and write the introductory text.
- Copied my q-learning struture from my older projects and prepared it as a template.
- Created virtual environment and intall dependicies
- Started to fill the gaps from the previous template.
- Created requirements.txt for easy deployment.
- I've got the create a struture of the q-table and state.
    - I am thinking to store the sate as simple range(9) array. However, I am not sure how to uniqully represent them as state number to easly hash into q-table.
    - Maybe I can check how joe has made it.
        - Gotcha! very clever he actually joins the elements of the state as string and uses that value as key to access q-table.
        - So I am filling the agent's getQ function accordinglly.
        - Or I can always keep the state as string. There is no need tto keep itt as array.
    - So q-table struture can be 2-dim array with state and action.
- I need to implement play  function into agent, hence there is going to be two different agents that will play one on one each other.
- Should update the q-table after a game has finished and back propagte with all actioins. Or Should I update q-table every round. Will move-on next day. The code curentlly is not runable.

#### 09.11.2020

- I am not sure how frequent should I update q-table, however from my blackjack project experience I am going to update and back propagate after the game ends.
    - Well also I have relized that Joe also did the sam way.
    - So I have copied the nececary update function into the agent class so that we can backpropagate for each agent seperatelly.
- I have coded so far that only the findWinner method is missing. Also in the agent class I need to select the random and greedy action properly among from the valid actions only.