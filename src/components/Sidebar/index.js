import React from 'react'
import { ProSidebar, SidebarHeader, Menu, MenuItem } from 'react-pro-sidebar'
import { BiBook, BiUser, BiCameraMovie } from 'react-icons/bi'
import { Link } from 'react-router-dom'
import './index.css'

const Sidebar = () => {
  return (
    <ProSidebar>
      <SidebarHeader className="sidebar-header">
        <Link to="/home" className="logo">
          <h2>EntreCOL+</h2>
        </Link>
      </SidebarHeader>
      <Menu iconShape="square">
        <Link to="/book">
          <MenuItem icon={<BiBook />}>Books</MenuItem>
        </Link>
        <Link to="/movie">
          <MenuItem icon={<BiCameraMovie />}>Movies</MenuItem>
        </Link>
        <Link to="/employee">
          <MenuItem icon={<BiUser />}>Employees</MenuItem>
        </Link>
      </Menu>
    </ProSidebar>
  )
}

export default Sidebar

// <ProSidebar>
//   <SidebarHeader className="sidebar-header">
//     <Link to="/home" className="logo">
//       <h2>EntreCOL+</h2>
//     </Link>
//   </SidebarHeader>
//   <Menu iconShape="square">
//     <MenuItem icon={<BiBook />}>
//       <Link to="/book">Books</Link>
//     </MenuItem>
//     <Link to="/movies">
//       <MenuItem icon={<BiCameraMovie />}>Movies</MenuItem>
//     </Link>
//     <Link to="/employees">
//       <MenuItem icon={<BiUser />}>Employee</MenuItem>
//     </Link>
//   </Menu>
// </ProSidebar>
