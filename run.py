import menu as RunMenu
import Rig_MCLP as rig
import SelectFile as file_select
import Constructive as constructive
import Constructive2 as constructive2
import LocalSearch as ls
import sys

# Run and get data for constructive from menu
option = RunMenu.menu()

# Execute based on menu
if option == 1:
    rig.runRIG()
    sys.exit()
elif option == 2:
    initial_data = file_select.GetCandidateAndDemand()
else:
    RunMenu.menu()  


# Set data for constructive
candidate = initial_data[0]
demand = initial_data[1]
p = initial_data[2]
f = initial_data[3]
sf = initial_data[4]
r = initial_data[5]

# Run and get results from worst constructive
c_data = constructive.Constructive(candidate, demand, p, f, sf, r)

# Set data for local search
c_demand = c_data[0]
c_candidate = c_data[1]
c_of = c_data[2]
c_sf = c_data[3]
c_r = c_data[4]
c_title = c_data[5]
c_p = c_data[6]
c_selected_sites = c_data[7]

# Run local search with previous results
ls.LocalSearch(c_demand, c_candidate, c_of, c_sf, c_r, c_title, c_p, c_selected_sites)

# Run and get results from constructive
c_data = constructive2.Constructive(candidate, demand, p, f, sf, r)

# Set data for local search
c_demand = c_data[0]
c_candidate = c_data[1]
c_of = c_data[2]
c_sf = c_data[3]
c_r = c_data[4]
c_title = c_data[5]
c_p = c_data[6]
c_selected_sites = c_data[7]

# Run local search with previous results
ls.LocalSearch(c_demand, c_candidate, c_of, c_sf, c_r, c_title, c_p, c_selected_sites)