class Resource(object):
    """
    Creatures get gold from Resources deposits that are scattered across the map.
    """

    def __init__(self, name, gold_amount, gold_flux):
        """
        :param: name The resource's name (eg: Tree, Gold Mine, etc)
        :param: gold_amount The amount of gold stored in this resource.
        :param: gold_flux The amount of gold that can be retrieved per turn by any creature.
        """
        self.name = name
        self.gold_amount = gold_amount
        self.gold_flux = gold_flux

    def depleted(self):
        return self.gold_amount <= 0

    def gather(self, gold_flux_cap=None):
        if self.depleted():
            return 0

        if gold_flux_cap:
            gold_extracted = min(gold_flux_cap, self.gold_flux)
        else:
            gold_extracted = self.gold_flux
        
        if self.gold_amount - gold_extracted > 0:
            self.gold_amount -= gold_extracted
            return self.gold_flux
        else:
            remaining_gold = self.gold_amount
            self.gold_amount = 0
            return remaining_gold