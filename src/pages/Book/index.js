import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Sidebar from '../../components/Sidebar'
import TableBook from '../../components/TableBook'

import './index.css'

const columns = [
  { title: 'Id', headerName: 'Id', field: 'bookID', width: 130 },
  { title: 'Title', headerName: 'Title', field: 'title', width: 400 },
  { title: 'Avarage Rating', headerName: 'Avarage Rating', field: 'average_rating', width: 120 },
  { title: 'Date', headerName: 'Date', field: 'publication_date', width: 100 },
  { title: 'Ratings Count', headerName: 'Ratings Count', field: 'ratings_count', width: 110 },
  { title: 'Idioma', headerName: 'Idioma', field: 'language_code', width: 75 },
  { title: 'Editorial', headerName: 'Publicator', field: 'publisher', width: 150 },
  { title: 'Autores', headerName: 'Autores', field: 'authors', width: 250 },
]

const Book = () => {
  const [data, setData] = useState([])
  const [pageSize, setPageSize] = useState(5)
  const [page, setPage] = useState(1)

  const getData = async () => {
    const url = `http://localhost:5000/books?_page=${page}&_limit=${pageSize}`
    const result = await axios.get(url)
    setData(result.data)
  }

  console.log(data)

  useEffect(() => {
    getData()
  }, [pageSize, page])

  const handleSelectedRows = (event) => {
    setPageSize(event.target.value)
  }

  return (
    <div className="container-book">
      <Sidebar />
      <div className="content">
        <h2>Books</h2>
        <TableBook
          rows={data.map((book) => book)}
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

export default Book
