#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2015 Gramps
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

register(GRAMPLET,
id    = 'Relid',
name  = _("Relation ID"),
description =  _("Shows person's relation, id, locator"),
version = '1.0.9',
gramps_target_version = '4.2',
include_in_listing = False,
status = STABLE,
fname = 'Relation_ID.py',
gramplet = 'IDGramplet',
height = 230,
expand = True,
gramplet_title = _("Who, What, Where, When on tree")
  )
