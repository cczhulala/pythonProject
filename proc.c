#include <linux/module.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h>

static struct proc_dir_entry *dir;
static struct proc_dir_entry *pfile;

static char msg[255];

static ssize_t myproc_read(struct file *file, char __user *buff, size_t count, loff_t *pos)
{
unsigned int len = strlen(msg);
unsigned long p = *pos;

if(p >= len)
    return 0;
if(count > len - p)
    count = len - p;
if(raw_copy_to_user(buff+p, msg+p, count))
    return -EFAULT;

*pos += count;
printk("read pos: %ld, count: %ld\n", p, count);
return count;
}

static ssize_t myproc_write(struct file *file, const char __user *buff, size_t len, loff_t *pos)
{
unsigned long len2 = len;
if(len2 >= sizeof(msg))
    len2 = sizeof(msg) - 1;
if(raw_copy_from_user (msg,buff,len2))
    return -EFAULT;

msg[len2] = '\0';
return len;
}
struct file_operations pfops = {
    .read = myproc_read,
    .write = myproc_write,
};
static int __init myproc_init(void)
{
dir = proc_mkdir("dir", NULL);
if(!dir){
printk(KERN_ERR "Can't create /proc/dir/nextdir\n");
remove_proc_entry("dir", NULL);
return -1;
}
printk(KERN_ERR "Create /proc/dir\n");
pfile = proc_create("nextdir", 0666, dir, &pfops);
if(!pfile){
printk(KERN_ERR "Can't create /proc/dir/nextdir\n");
remove_proc_entry("dir", NULL);
return -1;
}
printk(KERN_ERR "Create /proc/dir/nextdir\n");
return 0;
}

static void __exit myproc_exit(void)
{
remove_proc_entry("nextdir",dir);
remove_proc_entry("dir",NULL);
}

module_init(myproc_init);
module_exit(myproc_exit);

