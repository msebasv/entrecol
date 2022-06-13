import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Sidebar from '../../components/Sidebar'
import TableMovie from '../../components/TableMovie'

import './index.css'

const columns = [
  { title: 'Codigo', headerName: 'Codigo', field: 'codigo', width: 60 },
  { title: 'Title', headerName: 'Title', field: 'nombre', width: 450 },
  { title: 'Genero', headerName: 'Genero', field: 'generos', width: 300 },
]

const Movie = () => {
  const [data, setData] = useState([])
  const [pageSize, setPageSize] = useState(5)
  const [page, setPage] = useState(1)

  const getData = async () => {
    const url = `http://127.0.0.1:8000/peliculas?pagination=${page}&quantity=${pageSize}`
    const result = await axios.get(url)
    setData(result.data)
  }

  useEffect(() => {
    getData()
  }, [pageSize, page])

  const handleSelectedRows = (event) => {
    setPageSize(event.target.value)
  }

  return (
    <div className="container-movie">
      <Sidebar />
      <div className="content">
        <h2>Movies</h2>
        <TableMovie
          rows={data.map((movie) => movie)}
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

export default Movie
