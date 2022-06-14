// @mui
import Typography from "@mui/material/Typography";
import Box from '@mui/material/Box';
import Icon from "@mui/material/Icon";
import IconButton from "@mui/material/IconButton";
import AddIcon from '@mui/icons-material/Add';
import ModalFormInsertRequest from './modal';

export default function HeaderSection() {
  return (
    <Box
      sx={{
        pt: 4,
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
      }}
      >
      <Typography variant='h4'>
        Solicitudes
    </Typography>
      <ModalFormInsertRequest>
      <IconButton
        sx={{
          display: 'flex',
          borderRadius: 2,
          color: 'var(--btn-primary)',
          border: '1px solid var(--btn-primary)',
          fontWeight: 'bold',
          '&:hover': { background: 'var(--btn-gradient)', color: '#fff' },
        }}
      >

        <Icon>
          <AddIcon />
        </Icon>
      <Typography sx={{ fontWeight: 'inherit', fontSize: { lg: '1.15rem' } }}>
      Nueva solicitud
      </Typography>
      </IconButton>
      </ModalFormInsertRequest>
    </Box>
  )
}

