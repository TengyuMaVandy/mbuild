import mbuild as mb


class MPC(mb.Compound):
    """A 2-(methacryloloxy) ethyl phosophorylcholine monomer."""
    def __init__(self, alpha=0):
        super(MPC, self).__init__(self)

        # Look for data file in same directory as this python module.
        self.append_from_file('mpc.pdb', relative_to_module=self.__module__)

        # Transform the coordinate system of mpc such that the two carbon atoms
        # that are part of the backbone are on the y axis, c_backbone at the origin.
        C_top = self.atoms[37]
        # this can be achieved with the following alternative syntax:
        # C_top = self.labels["atom[37]"]
        # C_top = self.labels["atom"][37]
        C_bottom = self.atoms[1]

        mb.y_axis_transform(self, new_origin=C_top, point_on_y_axis=C_bottom)

        # Add top port.
        self.add(mb.Port(anchor=C_top), 'up')
        mb.translate(self.up, C_top - (C_top - C_bottom)*1.50)

        # Add bottom port
        self.add(mb.Port(anchor=C_bottom), 'down')
        mb.rotate_around_y(self.down, alpha)
        mb.translate(self.down, C_bottom - (C_bottom - C_top)*1.50)

if __name__ == "__main__":
    monomer = MPC()
    monomer.visualize(show_ports=True)
