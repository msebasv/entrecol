import React, {useState} from 'react'

import { Button, Select, MenuItem } from '@mui/material'

import {
  DataGrid,
  gridPaginatedVisibleSortedGridRowIdsSelector,
  GridToolbarContainer,
  useGridApiContext,
} from '@mui/x-data-grid'

import './index.css'

const getRowsFromCurrentPage = ({ apiRef }) =>
  gridPaginatedVisibleSortedGridRowIdsSelector(apiRef)

const CustomToolbar = () => {
  const apiRef = useGridApiContext()

  const handleExport = (options) => {
    apiRef.current.exportDataAsPrint(options)
  }

  return (
    <GridToolbarContainer>
      <Button
        onClick={() =>
          handleExport({ getRowsToExport: getRowsFromCurrentPage })
        }
      >
        Export PDF
      </Button>
    </GridToolbarContainer>
  )
}

function CustomPagination(props) {
  const { page, setPage, size, setSize } = props

  return (
    <div>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={size}
        label="Rows"
        onChange={setSize}
      >
        <MenuItem value={5}>5</MenuItem>
        <MenuItem value={10}>10</MenuItem>
        <MenuItem value={15}>15</MenuItem>
      </Select>
      <Button disabled={page <= 1} onClick={() => setPage(page - 1)}>
        Previous
      </Button>
      <Button onClick={() => setPage(page + 1)}>Next</Button>
    </div>
  )
}
const TableEmployee = (props) => {
  const { rows, columns, size, setSize, page, setPage } = props
  const [employee, setEmployee] = useState([{
        codigo: 0,
        nombre: "",
        dependencia: "",
        cargo: "",
        fecha_ingreso: 0,
        eps: "",
        pension: "",
        rol: ""
  }])

  const Test = () => (
    <CustomPagination
      page={page}
      setPage={setPage}
      size={size}
      setSize={setSize}
    />
  )

  const Employee = () => {
    const empleado = rows.map((employee) => {
      return ({
        codigo: employee.codigo,
        nombre: employee.nombre,
        dependencia: employee.dependencia.nombre,
        cargo: employee.cargo.nombre,
        fecha_ingreso: employee.fecha_ingreso,
        eps: employee.eps.nombre,
        pension: employee.pension.nombre,
        rol: employee.rol.nombre
      })
    })
    setEmployee(empleado)
    console.log(employee)
  }

  return (
    <div className="container-table">
      <DataGrid
        getRowId={(row) => row.codigo}
        rows={rows}
        columns={columns}
        rowsPerPageOptions={[5, 10 ,15]}
        components={{
          Toolbar: CustomToolbar,
          Pagination: Test,
        }}
        pagination
      />
    </div>
  )
}

export default TableEmployee
