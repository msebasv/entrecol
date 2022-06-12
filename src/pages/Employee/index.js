import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Sidebar from '../../components/Sidebar'
import TableEmployee from '../../components/TableEmployee'

import './index.css'

const columns = [
  { title: 'Codigo', headerName: 'Codigo', field: 'codigo', width: 60 },
  { title: 'Nombre', headerName: 'Nombre', field: 'nombre', width: 400 },
  { title: 'Dependencia', headerName: 'Dependencia', field: 'dependencia', width: 300 },
  { title: 'Cargo', headerName: 'Cargo', field: 'cargo', width: 70 },
  {
    title: 'Fecha Ingreso',
    headerName: 'Fecha Ingreso',
    field: 'fecha_ingreso',
    width: 70,
  },
  { title: 'Eps', headerName: 'Eps', field: 'eps', width: 100 },
  {
    title: 'Pension',
    headerName: 'Pension',
    field: 'pension',
    width: 120,
  },
  { title: 'Rol', headerName: 'Rol', field: 'rol', width: 110 },
]

const Employee = () => {
  const [data, setData] = useState([])
  const [pageSize, setPageSize] = useState(100)
  const [page, setPage] = useState(1)
  const [employee, setEmployee] = useState([])

  const getData = async () => {
    const url = `https://back-god.herokuapp.com/empleado?pagination=${page}&quantity=${10}`
    const result = await axios.get(url)
    setData(result.data)
  }

  useEffect(() => {
    getData()
  }, [pageSize, page])

  const handleSelectedRows = (event) => {
    setPageSize(event.target.value)
  }
  
  const Employee = () => {
    data.map((employee) => {
      const emp = {
        codigo: employee.codigo,
        nombre: employee.nombre
      }
      setEmployee(emp)
    })
  }




  return (
    <div className="container-employee">
      <Sidebar />
      <div className="content">
        <h2>Employee</h2>
        <TableEmployee
          rows={data.map((employee) => employee)}
          columns={columns}
          size={pageSize}
          setSize={handleSelectedRows}
          page={page}
          setPage={setPage}
        />
      </div>
    </div>
  )
}

export default Employee

